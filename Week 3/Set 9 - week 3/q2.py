# Write a Python program to show that we can create instance variables inside methods

class VariableNames(object):
    def __init__(self, s):
      s = "Class Variable Now"
      print("Initially ", s)
    def func1(self):
        self.s = "Inside func1"
        v = "Hello I am func1"
        print(v)
        print("In Func1 ", self.s)
    
    def func2(self):
        v = "Hello I am func2"
        print(v)
        self.s = "Inside func2"
        print("Func2", self.s)
        

s = "Global Scope"
vn = VariableNames(s)
vn.func1()
vn.func2()
print("At the end ",s)
