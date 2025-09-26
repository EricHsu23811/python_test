# 函式 function - https://youtu.be/zdMUJJKFdsU?si=WXJp_4tfXp2DwGRu&t=5695
def hello(name,age):
    print("Hello" + name +", 您今年"+str(age)+"歲")
    print("您好")   # 有縮排的行數會是function裡面的內容
hello("妮妮",5)

def add(num1,num2):
    print(num1+num2)
    return 10   # 如果沒有return，那就會return 'none'
    print("您好")   # return後面的內容將不會被執行

value=add(3,4)      # value=10，但進入add()會先print 3+4=7
print(add(3,2)*5)   # 先print 3+2=5, 再return 10, 10*5=50
print(value)
