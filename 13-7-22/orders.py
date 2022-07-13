# Design a food ordering system where your python program will run two threads,
# Place Order: This thread will be placing an order and inserting that into a queue. 
# This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
# This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

from queue.queue import Queue
from time import sleep
from threading import Thread, current_thread

class FoodOrderSystem:
    def __init__(self, orders):
        self.orders = orders
        self.q = Queue()

    def placeOrder(self):
        for order in self.orders:
            self.q.enqueue(order)
            print(f"{current_thread().name} - {order}.")
            sleep(0.5)

    def serveOrder(self):
        while not self.q.isEmpty():
            print(f"{current_thread().name} - {self.q.dequeue()}.")
            sleep(2)

    def run(self):
        t1 = Thread(target = self.placeOrder)
        t2 = Thread(target = self.serveOrder)
        t1.start()
        sleep(1)
        t2.start()

if __name__ == '__main__':
    fos = FoodOrderSystem(['pizza','samosa','pasta','biryani','burger'])
    fos.run()
