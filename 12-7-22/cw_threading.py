from threading import *
from time import sleep

def threadTask():
    for i in range(5):
        sleep(1)
        print("Iteration", i, " in ", current_thread().name)

t1 = Thread(target = threadTask)
t2 = Thread(target = threadTask)
t3 = Thread(target = threadTask)

t1.start()
t2.start()
t3.start()

print("Main Thread = ", current_thread().name)