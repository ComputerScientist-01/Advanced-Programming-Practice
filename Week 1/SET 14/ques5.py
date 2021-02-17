def MaxZero(ar,n) :
    l=[int(x) for x in ar.split()]
    z=0
    maxz=0
    maxval=0
    for x in l:
        s=str(x)
        no=[int(y) for y in s]
        z=no.count(0)
        if maxz<z:
            maxz=z
            maxval=x
        elif maxz==z and maxz!=0:
            maxval=max(maxval,x)
        del no
    if maxz==0:
        print(-1)
    else:
        print(maxval)

n=int(input())
ar=input()
MaxZero(ar,n)



