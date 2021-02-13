def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True

str = input("enter a sentence :\n ")
if ispangram(str):
    print('contains all alphabets')
else:
    print('does not contain all alphabets')
