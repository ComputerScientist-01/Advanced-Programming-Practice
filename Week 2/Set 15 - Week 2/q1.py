# Write a Python Program to Convert octal to binary, binary to decimal.

n = int(input('1. Octal to binary\n2.Binary to decimal:\n'))
c = int(input("Enter the no: "))

def OctToBin(octnum): 
      
    binary = "" 
    while octnum != 0: 
        d = int(octnum % 10) 
        if d == 0:  
            binary = "".join(["000", binary]) 
        elif d == 1: 
            binary = "".join(["001", binary]) 
        elif d == 2: 
            binary = "".join(["010", binary]) 
        elif d == 3:
            binary = "".join(["011", binary]) 
        elif d == 4:  
            binary = "".join(["100", binary]) 
        elif d == 5: 
            binary = "".join(["101", binary]) 
        elif d == 6:  
            binary = "".join(["110",binary]) 
        elif d == 7: 
            binary = "".join(["111", binary]) 
        else: 
            binary = "Invalid Octal Digit"
            break
  
        # updating the oct for while loop 
        octnum = int(octnum / 10)          
   
    return binary

def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base = 1;
     
    temp = num;
    while(temp):
        last_digit = temp % 10;
        temp = int(temp / 10);
         
        dec_value += last_digit * base;
        base = base * 2;
    return dec_value;

if n == 1:
    print("Octal to Binary Conv: ",OctToBin(c))
elif n == 2:
    print("Binary to Decimal Conv: ",binaryToDecimal(c))

else:
    print("Invalid input please try again")