class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length+=1
        self.getAll()

    def prepand(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length+=1
        self.getAll()

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
            return self.getAll()
        if index == 0:
            self.prepand(value)
            return self.getAll()
        newNode=Node(value)
        indexNode=self.getNodeByIndex(index-1)
        newNode.next=indexNode.next
        indexNode.next=newNode
        self.length+=1
        return self.getAll()

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return self.getAll()
        if index >= self.length:
            index = self.length - 1
        indexNode = self.getNodeByIndex(index-1)
        indexNode.next = indexNode.next.next
        self.length-=1
        return self.getAll()

    def reverse1(self):
        currentNode = self.head
        reversed = LinkedList(currentNode.value)
        for i in range(self.length-1):
            currentNode = currentNode.next
            reversed.prepand(currentNode.value)
        return reversed

    def reverse2(self):
        first = self.head
        second = first.next
        self.tail = self.head
        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp
        self.head.next = None
        self.head = first
        return self.getAll()


    def getNodeByIndex(self, index):
        indexNode = self.head
        for i in range(index):
            indexNode = indexNode.next
        return indexNode

    def getAll(self):
        list = []
        currentNode = self.head
        while currentNode:
            list.append({
                "current": currentNode.value,
                "next": currentNode.next.value if currentNode.next else None,
                 })
            currentNode = currentNode.next
        return list



a = LinkedList(10)
a.append(15)
a.append(17)
a.append(18)
print(a.getAll())
# a.prepand(168)
# a.insert(1, 25)
# a.remove(5)
print(a.reverse2())