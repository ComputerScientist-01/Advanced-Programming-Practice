n = int(input())

for i in range(1,n+1) :
    if i%5==0:
        continue
    if i*i == n:
        break
    print(i)