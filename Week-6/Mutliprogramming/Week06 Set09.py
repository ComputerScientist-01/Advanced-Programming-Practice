from threading import Semaphore, Thread
from time import sleep


running = True


def eating(index):
    print (f'Philosopher {index} starts eating.')
    sleep(30)
    print (f'Philosopher {index} finishes eating and leaves to think.')


def dine(forkL, forkR, index):
    while running:
        forkL.acquire() # wait operation on left fork
        locked = forkR.acquire(False) 
        #if right fork is not available leave left fork
        if locked:
            break 
        forkL.release()
        print (f'Philosopher {index} swaps forks.')
        forkL, forkR = forkR, forkL
    else:
        return
    eating(index)
    #release both the fork after eating
    forkR.release()
    forkL.release()


# Philosopher is thinking (but really is sleeping).
def thinking(index, forkL, forkR):
    while running:
        sleep(30)
        print (f'Philosopher {index} is hungry.')
        dine(forkL, forkR, index)




forks = [Semaphore(1) for i in range(5)] #initialising array of semaphore i.e forks

# here (i+1)%5 is used to get right and left forks circularly between 1-5
philosophers= [Thread(target=thinking, args=(i, forks[i%5], forks[(i+1)%5],)) for i in range(5)]

running = True
for p in philosophers: 
    p.start()

sleep(100)
running = False

print("Now we're finishing.")