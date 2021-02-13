tuple1 = tuple(map(int,input().split()))
tuple2 = tuple(map(int,input().split()))
tuple3 = tuple(map(int,input().split()))

adder = tuple(map(lambda x, y, z: (x + y + z)//3, tuple1, tuple2, tuple3))

print(adder)

