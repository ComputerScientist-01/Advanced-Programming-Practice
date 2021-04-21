from threading import Thread, Semaphore
from time import sleep
import random



MAX = 50
obj = Semaphore(0)


# acquire: decrement by 1
# release: increment by 1


# PRODUCER
def producer_func(name):
    n = random.randint(10,20)
    if obj._value+n <= MAX:
        for i in range(n):
            obj.release()
            print(name, 'number of items: ', obj._value)
            sleep(0.2)
    print('Producer finished')



# CONSUMER
def consumer_func(name):
    n = random.randint(1,20)
    if obj._value+n >= 0:
        for i in range(n):
            obj.acquire()
            print(name, 'number of items: ', obj._value)
            sleep(0.2)
    print('Consumer finished')



# creating multiple thread 
producer = Thread(target=producer_func, args=('PRODUCER: ',))
consumer = Thread(target=consumer_func, args=('CONSUMER: ',))



# calling the threads 
producer.start()
sleep(0.1)
consumer.start()



# waiting for threads to synchronize and end
producer.join()
consumer.join()
print('PRODUCER & CONSUMER HAVE FINISHED')