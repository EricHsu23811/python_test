# Q.ai的範例程式碼，做為參考用
import logging
from enum import Enum
from pathlib import Path
from types import TracebackType
from typing import Type, cast

import av
import clr  # type: ignore
import numpy as np
import numpy.typing as npt

DLL_PATH = Path(__file__).parent.parent.parent / "libs" / "win64" / "DirectShowLib.dll"
clr.AddReference(str(DLL_PATH))
from DirectShowLib import (
    DsDevice,
    FilterCategory,
    IAMCameraControl,
    IAMVideoProcAmp,
    VideoProcAmpFlags,
    VideoProcAmpProperty,
)
from System import Guid
from System.Runtime.InteropServices import Marshal

logger = logging.getLogger(__name__)


CAMERA_FILTER_IID = "56A86895-0AD4-11CE-B03A-0020AF0BA770"


class GetPropertyError(RuntimeError): ...


class DshowGetterResultIdx(int, Enum):
    STATUS_CODE = 0
    VALUE = 1


class ControlToVideoProcAmpMapping(Enum):
    GAIN = VideoProcAmpProperty.Gain
    EXPOSURE__100US = VideoProcAmpProperty.Brightness
    LASER_STATUS = VideoProcAmpProperty.BacklightCompensation
    LASER_POWER__DN = VideoProcAmpProperty.Saturation


class QWebcam:
    MIN_EXPOSURE__US = 0
    MAX_EXPOSURE__US = 10000
    MIN_LASER_POWER__DN = 0
    MAX_LASER_POWER__DN = 65
    MIN_GAIN = 1
    MAX_GAIN = 16
    LASER_OFF_VALUE = 1
    LASER_ON_VALUE = 2
    DEFAULT_FPS = 100

    def __init__(self, camera_name: str, fps: int = DEFAULT_FPS) -> None:
        self.name = camera_name
        self.fps = fps

        devices = DsDevice.GetDevicesOfCat(FilterCategory.VideoInputDevice)
        for device in devices:
            if camera_name in device.Name:
                iid = Guid(CAMERA_FILTER_IID)
                logger.info(f"Connecting to camera '{camera_name}'...")
                self.camera_filter = device.Mon.BindToObject(None, None, iid)[DshowGetterResultIdx.VALUE]
                self.proc_amp = IAMVideoProcAmp(self.camera_filter)
                self.cam_control = IAMCameraControl(self.camera_filter)
                logger.info(f"Successfully connected to camera '{camera_name}'")
                return

        raise ValueError(f"Camera '{camera_name}' not found. Available cameras: {[device.Name for device in devices]}")

    def __enter__(self) -> "QWebcam":
        frame_grabbing_options = {"framerate": str(self.fps)}
        self.frame_grabber = av.open(f"video={self.name}", format="dshow", options=frame_grabbing_options)
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def close(self) -> None:
        self.frame_grabber.close()

        for obj in [self.cam_control, self.proc_amp, self.camera_filter]:
            if obj:
                Marshal.ReleaseComObject(obj)

        self.cam_control = self.proc_amp = self.camera_filter = None
        logger.info("Camera resources released")

    def get_next_frame(self) -> npt.NDArray[np.uint8]:
        frame = next(self.frame_grabber.decode(video=0))
        return cast(npt.NDArray[np.uint8], frame.to_ndarray(format="gray"))

    def _validate_input(self, control_name: str, min_value: int, max_value: int, value: int) -> None:
        if not (min_value <= value <= max_value):
            raise ValueError(f"Invalid value for {control_name}: {value}. Must be between {min_value}-{max_value}.")

    def _set_property(self, property: ControlToVideoProcAmpMapping, value: int) -> None:
        logger.info(f"Setting {property.name.lower()} to {value}")
        self.proc_amp.Set(property.value, value, VideoProcAmpFlags.Manual)

    def _get_property(self, property: ControlToVideoProcAmpMapping) -> int:
        result = self.proc_amp.Get(property.value)
        if result[DshowGetterResultIdx.STATUS_CODE] != 0:
            raise GetPropertyError(
                (
                    f"Failed to get property {property.name.lower()}. "
                    f"Error status code: {result[DshowGetterResultIdx.STATUS_CODE]}"
                )
            )

        logger.info(f"Current {property.name.title()}: {result[DshowGetterResultIdx.VALUE]}")
        return result[DshowGetterResultIdx.VALUE]

    def set_laser_status(self, laser_status: bool) -> None:
        value = self.LASER_ON_VALUE if laser_status else self.LASER_OFF_VALUE
        self._set_property(ControlToVideoProcAmpMapping.LASER_STATUS, value)

    def get_laser_status(self) -> bool:
        laser_status_value = self._get_property(ControlToVideoProcAmpMapping.LASER_STATUS)
        return laser_status_value == self.LASER_ON_VALUE

    def set_laser_power__dn(self, laser_power__dn: int) -> None:
        self._validate_input("Laser Power", self.MIN_LASER_POWER__DN, self.MAX_LASER_POWER__DN, laser_power__dn)
        self._set_property(ControlToVideoProcAmpMapping.LASER_POWER__DN, laser_power__dn)

    def get_laser_power__dn(self) -> int:
        laser_power = self._get_property(ControlToVideoProcAmpMapping.LASER_POWER__DN)
        return laser_power

    def set_gain(self, gain: int) -> None:
        self._validate_input("Gain", self.MIN_GAIN, self.MAX_GAIN, gain)
        self._set_property(ControlToVideoProcAmpMapping.GAIN, gain)

    def get_gain(self) -> int:
        gain = self._get_property(ControlToVideoProcAmpMapping.GAIN)
        return gain

    def set_exposure__us(self, exposure__us: int) -> None:
        self._validate_input("Exposure", self.MIN_EXPOSURE__US, self.MAX_EXPOSURE__US, exposure__us)
        if exposure__us % 100 != 0:
            raise ValueError(f"Exposure must be a multiple of 100. Given: {exposure__us}us")

        exposure__100us = exposure__us // 100
        self._set_property(ControlToVideoProcAmpMapping.EXPOSURE__100US, exposure__100us)

    def get_exposure__us(self) -> int:
        exposure__100us = self._get_property(ControlToVideoProcAmpMapping.EXPOSURE__100US)
        exposure__us = exposure__100us * 100
        return exposure__us
