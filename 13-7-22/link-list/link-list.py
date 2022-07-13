class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtBeginning(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.length += 1

    def insertAtIndex(self, index, data):
        if index == 0:
            self.insertAtBeginning(data)
            return

        if index < 0 or index >= self.length:
            return "Index out of bounds! Cannot insert."

        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next
        
        newNode = Node(data, ptr.next)
        ptr.next = newNode
        self.length += 1

    def removeFromBeginning(self):
        if self.length == 0:
            return "Link List size is 0! Cannot remove."

        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return f"Removed {data} at index 0."


    def removeFromIndex(self, index):
        if self.length == 0:
            return "Link List size is 0! Cannot remove."

        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next

        data = ptr.next.data
        ptr.next = ptr.next.next
        self.length -= 1
        return f"Removed {data} at index {index}."

    def insertAfterValue(self, value, data):
        ptr = self.head
        while ptr.data != value:
            ptr = ptr.next
            if not ptr:
                return "Value not found."

        newNode = Node(data, ptr.next)
        ptr.next = newNode
        self.length += 1

    def removeByValue(self, value):
        if value == self.head.data:
            self.removeFromBeginning()
            return

        ptr = self.head
        while ptr.next.data != value:
            ptr = ptr.next
            if not ptr.next:
                return "Value not found."

        ptr.next = ptr.next.next
        self.length -= 1
        return "Removed {value}."
    
    def displayLinkList(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end = " ")
            ptr = ptr.next
        print('\n')


if __name__ == '__main__':
    ll = LinkList()

    ll.insertAtBeginning(4)
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(1)
    ll.displayLinkList()
    ll.insertAtIndex(2, 5)
    ll.displayLinkList()

    # print(ll.removeFromIndex(1))
    # ll.displayLinkList()
    # print(ll.removeFromBeginning())
    # ll.displayLinkList()
    # print(ll.removeFromIndex(2))
    # ll.displayLinkList()

    print(ll.insertAfterValue(12, 6))
    ll.displayLinkList()

    print(ll.removeByValue(12))
    ll.displayLinkList()

