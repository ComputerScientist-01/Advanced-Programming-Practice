# 3. Write a Python program to execute a string containing Python code.

# s = input("Enter a string to execute:\n")

s = '''
a = 80
b = 70
diff = a-b
print(diff)
    '''

exec(s)
