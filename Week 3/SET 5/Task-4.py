limit=0
print("Which package do you have A, B, or C? : ")
package =str(input())

if package in {'A', 'B', 'C'}:
    print("How many hours were used:")
    hours=int(input())
    if(hours > 744 or hours < 0):
        print("Hours cannot be greater than 744 or less than 0!! \n\n")
        print("Enter hours again: ")
        hours=int(input())

if package == "A":
    limit = 9.95;

    total = limit if (hours < 10) else ((hours - 10) * 2) + limit
    print("The amount due is: $%.2f"%total)

elif package == 'B':
    limit = 14.95;
    total = limit if (hours < 20) else ((hours - 20) * 1) + limit
    print("The amount due is: $%.2f"%total)

elif package == 'C':
    limit = 19.95;
    total = limit;
    print("The amount due is: $%.2f"%total)
