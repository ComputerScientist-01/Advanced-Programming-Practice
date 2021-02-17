import math
lambda_volume = lambda r: (4/3)*r*r*r*math.pi 
lambda_area = lambda r: 4*r*r*math.pi

r=int(input("Enter value of r : "))
print(lambda_area(r))
print(lambda_volume(r))

