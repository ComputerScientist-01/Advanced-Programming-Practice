arr = tuple(map(int,input().split()))

adderp = sum(list(filter(lambda x: (x>= 0) , arr)))
addernp = sum(list(filter(lambda x: (x<0) , arr)))

print(adderp)
print(addernp)

