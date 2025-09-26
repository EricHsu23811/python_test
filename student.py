from person import Person  # inheritance.py有參考到，繼承person
class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school

#    def print_name(self):
#        print(self.name)   # 已經繼承Person因此可以不用重複定義

#    def print_age(self):
#        print(self.age)    # 已經繼承Person因此可以不用重複定義

    def print_school(self):
        print(self.school)