# module模組   # https://youtu.be/zdMUJJKFdsU?si=EJroxmaWolfSz97o&t=12268
# 可google查詢python module list，找到 https://docs.python.org/3/py-modindex.html，可查到很多python內建的模組
import tool # 不需要輸入.py
import time # python內建的模組之一
import sys  # 內建模組路徑

# pip套件管理工具   #第三方擴充模組，比如Numpy => 可在terminal中輸入 pip install numpy 就會開始安裝
import numpy # Numpy安裝完成就可以import進來
print(numpy.abs(-12.3))

import numpy as NP  # 將numpy改名稱為NP，較方便使用
print(NP.abs(-45.6))

print(tool.name)

print(tool.max_num(3,5,87))

a = 3
print(time.localtime())

print(sys.path) # 列出內建模組的路徑位置列表