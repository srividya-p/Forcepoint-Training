from collections import deque

class Queue:
    def __init__(self, initialList = []):
        self.container = deque(reversed(initialList))

    def enqueue(self, value):
        self.container.appendleft(value)
        return f"{value} inserted in Queue."

    def dequeue(self):
        if self.isEmpty():
            return "Cannot dequeue! Queue is empty."
        return self.container.pop()

    def front(self):
        if self.isEmpty():
            return "Cannot peek! Stack is empty."
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return self.size() <= 0

if __name__ == "__main__":
    q = Queue([1, 2, 3, 4, 5])
    print(q.container)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.front())
    print(q.enqueue(6))
    print(q.container)