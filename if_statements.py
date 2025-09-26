# https://youtu.be/zdMUJJKFdsU?si=lQuwhvk5ZQwqVFqe&t=6884
# if判斷句

# 1.
# hungry=True
# if(hungry):
#     print("Go finding some food.")


# rainy = True
# if rainy:
#     print("Drive car to work.")
# else:
#     print("Walk to work.")


score=61
rainy=True
if score==100 and rainy:    # 且：and
    print("恭喜，獎金1000元")
elif score>=80:
    print("獎金80元")
elif score>=60:
    print("獎金60")
elif score!=0 or not(rainy):   # 或：or
    print("請再接再厲")
else:
    print("請補考")


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    if num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
num1=10
num2=5 
num3=7
print(max_num(num1,num2,num3))
print(max(num1,num2,num3))  # should be the same as the function above

