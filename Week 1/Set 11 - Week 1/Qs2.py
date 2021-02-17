# 2:Create a multiplication table asking the user the number of rows and columns he wants.
# Write a python program to implement the above table.

mul = int(input("Enter the value for the multiplication table: "))
upto = int(input("Enter the value upto which it will be shown: "))
res = dict()
for i in range(upto+1):
    res[i] = mul*i

print("The value as required is: ")
print(res)