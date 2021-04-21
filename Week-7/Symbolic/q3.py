from sympy import *

# Q1
a = Symbol('a')
da = diff(a**2, a)

ans1 = a * da
print(ans1)

# Qs2
x = Symbol('x')
y = Symbol('y')

ans2 = 2 * x + y**2
print(ans2)

#Qs3

ans3 = Rational(1,10) + Rational(1,5)
print(ans3)

# Qs4

ans4 = diff(sin(x), x)
print(ans4)