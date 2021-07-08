# 5.Write a Python program to create a dictionary from two lists without losing duplicate
# values.


a = [1,2,3,4,5,6,4]
b = [9,8,7,6,5,4,3]

m = {}

if (len(a) >= len(b)):
    for i in range(len(a)):            
        if i < len(b):
            if a[i] in m:
                m[a[i]].append(b[i])
            else:
                val = [b[i]]
                m[a[i]] = val
        else:
            m[a[i]] = None
else:
    for i in range(len(b)):            
        if i < len(a):
            if b[i] in m:
                m[b[i]].append(a[i])
            else:
                val = [a[i]]
                m[b[i]] = val
        else:
            m[b[i]] = None
print(m)