# touple(元組) -- https://youtu.be/zdMUJJKFdsU?si=owDsi7fsnPi40yOw&t=5355
# touple vs list(很相似):資料型態touple一旦建立就不能新增、修改、刪除，防止意外被新增/修改/刪除
scores = (90,80,60,70,50)   # list用[]，touple則用()來定義
print(scores[0:2])
print(len(scores))
# scores[0] = 30  #=> TypeError: 'tuple' object does not support item assignmen
print(scores)