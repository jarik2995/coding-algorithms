class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = newNode
        self.length+=1
        self.getAll()

    def prepand(self, value):
        newNode = Node(value)
        self.head.previous = newNode
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
        followerNode=self.getNodeByIndex(index-1)
        newNode.next=followerNode.next
        newNode.previous=followerNode
        followerNode.next=newNode
        self.length+=1
        return self.getAll()

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.previous=None
            return self.getAll()
        if index >= self.length - 1:
            self.tail = self.tail.previous
            self.tail.next = None
            return self.getAll()
        followerNode = self.getNodeByIndex(index-1)
        indexNode = followerNode.next
        leaderNode = indexNode.next
        followerNode.next = leaderNode
        leaderNode.previous = followerNode
        self.length-=1
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
                "previous": currentNode.previous.value if currentNode.previous else None
                 })
            currentNode = currentNode.next
        return list



a = LinkedList(10)
a.append(15)
a.append(17)
a.prepand(168)
a.insert(0, 25)
a.remove(4)
print(a.getAll())