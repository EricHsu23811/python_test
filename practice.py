# 問答程式 https://youtu.be/zdMUJJKFdsU?si=-oJV369utyUOuzRw&t=13466
from question import Question   # 只引入question.py裡面的Question類別
# import question     # 引入question.py裡面所有的類別(包括Question類別與變數a)

test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於幾公分？\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是甚麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
]
# print(test[0])

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score +=1

    print("你得到" + str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)