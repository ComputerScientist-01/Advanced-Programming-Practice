from time import sleep
from threading import Thread

def task(i):
    print(f'Hello from thread {i}')
    sleep(1)

n=50
for i in range(n,0,-1):
    t = Thread(target=task, args=(i,))
    t.start()
    sleep(0.1)