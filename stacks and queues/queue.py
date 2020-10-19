class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = self.first
            self.length+=1
        self.last.next = newNode
        self.last = newNode
        return self

    def dequeue(self):
        self.first = self.first.next
        self.length-=1
        return self


class QueueStacks():
    def __init__(self):
        self.first = []
        self.last = []

    def peek(self):
        if self.first:
            return self.first[-1]
        else
            return self.last[0]

    def enqueue(self, value):
        for i in range(self.first):
            self.last.append(self.first.pop())
        self.last.append(value)
        return self

    def dequeue(self):
        for i in range(self.last):
            self.first.append(self.last.pop())
        self.first.pop()
        return self

a = Queue()
a.enqueue(10)
a.enqueue(15)
a.dequeue()
print(a.peek())