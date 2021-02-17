# 4. Write a Python program to create a dictionary of keys x, y, and z where each key has as
# value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
# from the dictionary.

m = dict()
li = ['x','y','z']
s = 11;
for l in li:
    val = list()
    for i in range(9):
        val.append(s)
        s+=1
    s = s+1
    m[l] = val
print(m)
for k in m.keys():
    print(m[k][4])