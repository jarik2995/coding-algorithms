class Graph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes+=1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        for node,edges in self.adjacentList.items():
            print("%s--->%s" % (node,",".join(edges)))

a = Graph()
a.addVertex("0")
a.addVertex("1")
a.addVertex("2")
a.addVertex("3")
a.addVertex("4")
a.addVertex("5")
a.addVertex("6")
a.addVertex("7")
a.addEdge("0","1")
a.addEdge("0","2")
a.addEdge("1","2")
a.addEdge("1","3")
a.addEdge("2","4")
a.addEdge("3","4")
a.addEdge("4","5")
a.addEdge("5","6")

a.showConnections()