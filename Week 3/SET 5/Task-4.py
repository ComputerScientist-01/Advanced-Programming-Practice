limit=0
print("Which package do you have A, B, or C? : ")
package =str(input())

if(package == 'A'or package == 'B'or package == 'C'):
    print("How many hours were used:")
    hours=int(input())
    if(hours > 744 or hours < 0):
        print("Hours cannot be greater than 744 or less than 0!! \n\n")
        print("Enter hours again: ")
        hours=int(input())

if(package == "A"):

    limit = 9.95;
    
    if(hours < 10):
        total = limit;

    else:
        total = ((hours - 10) * 2) + limit

    print("The amount due is: $%.2f"%total)

if(package == 'B'):

    limit = 14.95;
    if(hours < 20):
        total = limit;
    else:
        total = ((hours - 20) * 1) + limit;

    print("The amount due is: $%.2f"%total)

if(package == 'C'):

    limit = 19.95;
    total = limit;
    print("The amount due is: $%.2f"%total)
