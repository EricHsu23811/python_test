#這是註解測試
print('Python test.測試')
print("Eric Test")
print("身高 170cm")

#基本資料型態

#字串
name = "妮妮"+'Cat'
print(name)

#數字
a = -70.001
print(a)

#布林值
is_cat = True
is_bad = False

# 1. 變數名稱只能是英文o數字or_的組合
# 2. 變數的開頭不可以是數字

print("有一隻貓叫做\n" + name)

# print out - Hello, "妮妮"
print('Hello \"妮妮\"')

# 函式 function
print(name.lower())
print(name.islower())
print(name.upper())
print(name.isupper())
print(name.upper().isupper())
# print("name isupper? "+ name.isupper()) => NG
print("name isupper? = "+ str(name.isupper()))
print(name[0] +","+ name[2])
print(name.index("妮"))
print(name.replace("妮妮", "Nini"))

# 如何使用數字
print(8/5)
print(8//5) #取整數部分
print(8%5) #取餘數
print("8/5 = " + str(8//5) + "..." + str(8%5))
print(abs(-8))  #絕對值
print(pow(2,4)) #2的4次方
print(max(-2,3,88,100))  #回傳後面數字中最大值
print(min(-2,3,88,100))  #回傳後面數字中最小值
print(round(4.6))   #回傳4捨5入的值
 
from math import *  #模組的引入：若無此行，底下的floor & ceil都會無效
print(floor(4.6))   #回傳無條件捨去值
print(ceil(4.4))   #回傳無條件進位值
print(sqrt(16)) #開根號
