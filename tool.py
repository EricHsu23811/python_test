# 搭配module.py，當成一個module使用
name = "妮"
age = "5"

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    if num2>=num1 and num2>=num3:
        return num2
    else:
        return num3