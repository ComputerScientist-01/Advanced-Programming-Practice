from functools import reduce
import math

a = [19, 41, 92, 67, 53]
b = [13, 61, 92, 31, 69]

mean_a = sum(a)/len(a)
mean_b = sum(b)/len(b)

def SD(x, y):
    f = (y-mean_a)**2   
    return x+f

sd_a = math.sqrt(reduce(SD, a, 0)/len(a))
sd_b = math.sqrt(reduce(SD, b, 0)/len(b))

print(sd_a)
print(sd_b)

if sd_a > sd_b:
    print("A is better")
else:
	print("B is better")