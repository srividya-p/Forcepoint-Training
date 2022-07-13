from collections import deque

class Stack:
    def __init__(self, initialList = []):
        self.container = deque(initialList)

    def push(self, value):
        self.container.append(value)
        return f"{value} inserted in Stack."

    def pop(self):
        if self.isEmpty():
            return "Cannot pop! Stack is empty."
        return self.container.pop()

    def peek(self):
        if self.isEmpty():
            return "Cannot peek! Stack is empty."
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return self.size() <= 0


if __name__ == "__main__":
    st = Stack([1, 2, 3, 4, 5])
    print(st.pop())
    print(st.push(6))
    print(st.size())
    print(st.peek())