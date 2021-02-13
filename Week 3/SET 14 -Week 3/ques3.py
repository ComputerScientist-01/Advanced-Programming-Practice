class ques3():
    
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

l = int(input())
w = int(input())
obj = ques3(l,w)
print(obj.rectangle_area())
