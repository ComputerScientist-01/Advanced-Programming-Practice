# 4. Write a Python program to create a dictionary of keys x, y, and z where each key has as
# value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
# from the dictionary.

m = {}
li = ['x','y','z']
s = 11;
for l in li:
    val = []
    for _ in range(9):
        val.append(s)
        s+=1
    s += 1
    m[l] = val
print(m)
for k, v in m.items():
    print(v[4])