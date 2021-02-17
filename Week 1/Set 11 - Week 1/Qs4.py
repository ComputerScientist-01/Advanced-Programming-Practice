# 4: Write a python program using structured paradigms concepts to compute the sum of the
# two given integers. If the two values are same, then returns triple their sum.

a = int(input("Enter any number: "))
b = int(input("Enter any number: "))

if a != b:
    print("The sum is", a+b)
else:
    print("The sum is", 3*(a+b))