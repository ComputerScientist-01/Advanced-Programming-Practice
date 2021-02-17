# Write a Python program to show that the variables with a value assigned in class
# declaration, are class variables and variables inside methods and constructors are
# instance variables.

class VariableNames(object):
    def __init__(self, s):
      s = "Class Variable Now"
      print("Initially ", s)
    def func1(self):
        self.s = "Inside func1"
        print("In Func1 ", self.s)
    
    def func2(self):
        self.s = "Inside func2"
        print("Func2", self.s)
        

s = "Global Scope"    
print("Execution Begins", s)
vn = VariableNames(s)
vn.func1()
vn.func2()
print("At the end ",s)
