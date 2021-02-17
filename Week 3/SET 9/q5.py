# Write a Python program to demonstrate that hidden members can be accessed outside
# a class

class Hidden():
    __hid = "I am hidden"
    
h = Hidden()
print(h._Hidden__hid)
# print(h.__hid)  Error printed if executed