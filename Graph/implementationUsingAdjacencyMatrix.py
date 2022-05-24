class Graph:
    def __init__(self,nVertices):
        self.nVertices  = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]


    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1


    def removeEdge(self,v1,v2):
        if self.conainsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v1][v2] = 0

    def conainsEdge(self,v1,v2):
        return self.adjMatrix[v1][v2] > 0

    def __str__(self):
        return str(self.adjMatrix)


g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
print(g)


