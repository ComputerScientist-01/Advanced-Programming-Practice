def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(char in str.lower() for char in alphabet)

str = input("enter a sentence :\n ")
if ispangram(str):
    print('contains all alphabets')
else:
    print('does not contain all alphabets')
