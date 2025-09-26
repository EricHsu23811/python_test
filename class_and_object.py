# https://youtu.be/zdMUJJKFdsU?si=WmEsZBU224RImgMT&t=12893
# 類別class、物件object
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

# https://youtu.be/zdMUJJKFdsU?si=K6K9_CBw4Yir_u1s&t=14069
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
        
    def add(self,num1,num2):
        return num1 + num2

phone1 = Phone("ios","0987654321",True)  # phone1就是一個object
print(phone1.number)
phone2 = Phone("android","0912345678",False)
print(phone2.os)

print(phone1.is_ios())
print(phone2.is_ios())

print(phone1.add(2,3))
