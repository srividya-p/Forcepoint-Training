from queue import Queue

def printBinary(n):
    q = Queue(['1'])
    for _ in range(n):
        front = q.front()
        print(front)
        q.enqueue(front + '0')
        q.enqueue(front + '1')
        q.dequeue()

printBinary(10)