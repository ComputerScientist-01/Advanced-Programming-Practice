# 2. Write a Python function that prints out the first n rows of Pascals triangle

n = int(input("Enter the value of n: "))
def pascal_triangle(num):
    row = [1]
    y = [0]
    for x in range(max(num,0)):
      print(row)
      row=[l+r for l,r in zip(row+y, y+row)]
    return num>=1
pascal_triangle(n) 