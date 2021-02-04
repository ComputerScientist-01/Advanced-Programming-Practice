def in_range(x,l,u):
   if x in range(l,u):
    print("is in the range ")
   else:
    print("Not in range")

x=int(input("Enter a number"))
l=int(input("Enter lower range"))
u=int(input("Enter a upper range"))

in_range(x,l,u)