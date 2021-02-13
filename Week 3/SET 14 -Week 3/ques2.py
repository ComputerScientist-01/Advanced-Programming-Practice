class ques2:

    def __init__(self):
        pass

    def _getString(self):
        s = input()
        return s
        
    def _printString(self,s):
        print(s.upper())

obj =  ques2()
s = obj._getString()
obj._printString(s)
        