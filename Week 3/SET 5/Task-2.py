class Student:
    def __init__(self):
        self.name = input("Enter your name:")
        self.roll = int(input("Enter your roll number:"))
        self.marks=list()
        for i in range (5):
            self.marks.insert(i,int(input("enter %d th mark :"%(i+1))))


class Test(Student):
    def check(self):
        print("Your average is", sum(self.marks)/5)

class Admin(Test):
    def display(self):
        print("=== Student info is ===")
        print("Name is : ", self.name)
        print("Roll number is : ", self.roll)

obj = Admin()
obj.check()
obj.display()
