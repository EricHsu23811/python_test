# List的用法 - https://youtu.be/zdMUJJKFdsU?si=O-cE2qwzkDYoEUVq&t=4142
scores = [90,70,60,50,80]
friends = ["小白","小藍","小紅"]
things = [87,"白藍",True]
print(scores)
print(friends)
print(things)
print(friends[0] + "'s score = " + str(scores[0]) )
print(scores[-2])   #倒數第2位
print(scores[1:4])  #第1位開始向後取到第4位之前(不包括第4位)
print(scores[1:])   #從第1位開始取到最後一位
print(scores[:4])   #從該之前一位(不含該位)往前取到最前面
scores[0] = 30
print(scores)

# extend用法

scores.append(30)
scores.insert(2,50) #第2位插入50這個值
scores.remove(50) #移除第一個50這個值
print(scores)

scores.pop()    #移除列表最後一位
print(scores)

scores.sort()   #由小到大排序
print(scores)

scores.clear()  #清除所有
print(scores)

scores.extend(friends)  #延伸加入另外一個list
print(scores)

scores.reverse()    #list反轉
print(scores)
print(scores.index("小白"))
print(scores.count("小白"))   #有幾個"小白"
