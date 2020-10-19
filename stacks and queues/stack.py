class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def pop(self):
        if self.length <= 1:
            self.top = None
            self.bottom = None
            self.length = 0
            return self
        self.top = self.top.next
        self.length-=1
        return self

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
            self.length = 1
            return self
        newNode.next = self.top
        self.top = newNode
        self.length+=1
        return self

    def peek(self):
        return self.top



class StackArray():
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        return self

    def pop(self):
        self.data.pop()
        return self

    def peek(self):
        return self.data[-1]

a = StackArray()
a.push(1)
a.push(2)
a.push(3)
a.pop()
print(a.peek())