# Write a python program to access hidden variable outside the class using object and
# which threw an exception.

class Hidden():
    __hid = "I am hidden"
    
h = Hidden()
# print(h._Hidden__hid)
try:
	print(h.__hid)
except Exception as e:
    print("Hidden variables cannot be accessed")