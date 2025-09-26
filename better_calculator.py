# https://youtu.be/zdMUJJKFdsU?si=dAP2nC2ZarNMN5Rh&t=8386
# 建立一個計算機
num1 = float(input("請輸入1st數字： "))
op = input("請輸入運算符號： ")
num2 = float(input("請輸入2nd數字： "))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("不支援此運算")