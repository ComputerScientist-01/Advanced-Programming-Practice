import threading
import random

global x              
x = 0
wlock = threading.Lock()
rlock = threading.Lock()

def Reader():
    global x
    try:
        wlock.acquire()
        print('Reader is Reading!')
        print('Shared Data:', x)
        wlock.release()
        print()
    except:
        print("Reader couldn't read, as Writing is taking place.")

def Writer():
    global x
    try:
        wlock.acquire()
        rlock.acquire()
        print('Writer is Writing!')
        x += 1
        print('Writer is Releasing the lock!')
        wlock.release()
        rlock.release()
        print()
    except:
        print("Writer couldn't write, as Reading or Writing is taking place.")

if __name__ == '__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100) 
        if(randomNumber > 50):
            threading1 = threading.Thread(target = Reader)
            threading1.start()
        else:
            threading2 = threading.Thread(target = Writer)
            threading2.start()

threading1.join()
threading2.join()

print("Final value : ",x)