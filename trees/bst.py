class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None


    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return self
        leafNode = self.findLeaf(self.root, value)
        if value < leafNode.value:
            leafNode.left = newNode
        elif value > leafNode.value:
            leafNode.right = newNode
        else:
            return None
        return self


    def lookup(self, value):
        if not self.root:
            return None
        node = self.findLeaf(self.root, value)
        if node.value == value:
            return node
        else:
            return None

    def remove(self, value):
        if not self.root:
            return None
        parentNode = self.getParentNode(value)
        if parentNode and parentNode.value > value:
            currentNode = parentNode.left
        elif parentNode and parentNode.value < value:
            currentNode = parentNode.right
        else:
            currentNode = self.root
        leafNode = currentNode.right
        parentleafNode = None
        while leafNode:
            if not leafNode.left:
                break
            parentleafNode = leafNode
            leafNode = leafNode.left
        if parentleafNode:
            parentleafNode.left = leafNode.right
            leafNode.right = currentNode.right
        if leafNode:
            leafNode.left = currentNode.left
        else:
            leafNode = currentNode.left
        if not parentNode:
            self.root = leafNode
        elif parentNode.value > value:
            parentNode.left = leafNode
        else:
            parentNode.right = leafNode
        return self



    def getParentNode(self, value):
        parentNode = self.root
        if value < parentNode.value:
            childNode = parentNode.left
        elif value > parentNode.value:
            childNode = parentNode.right
        else:
            return None
        while childNode:
            if value < childNode.value:
                parentNode = childNode
                childNode = childNode.left
            elif value > childNode.value:
                parentNode = childNode
                childNode = childNode.right
            else:
                return parentNode
            return None

    def findLeaf(self, node, value):
        print("Current node value: %d" % node.value)
        if value < node.value: # left
            print("%d < %d: going left" % (value, node.value))
            if not node.left:
                return node
            else:
                return self.findLeaf(node.left, value)
        elif value > node.value: # right
            print("%d > %d: going right" % (value, node.value))
            if not node.right:
                return node
            else:
                return self.findLeaf(node.right, value)
        else:
            print("%d = %d: returning" % (value, node.value))
            return node

#        9
#      8   20
#          15   30

a = BST()
a.insert(9)
a.insert(20)
a.insert(8)
a.insert(30)
a.insert(15)
a.remove(9)
print("sf")
print(a.lookup(8).value)