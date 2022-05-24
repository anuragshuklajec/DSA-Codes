class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        return self.adjMatrix[v1][v2] > 0

    def __str__(self):
        return str(self.adjMatrix)

    def __hasPathHelper(self,v1,v2,visited):
        if v1 == v2 or self.adjMatrix[v1][v2] > 0:
            return True
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] == False:
               if self.__hasPathHelper(i,v2,visited):
                   return True
        return False

    def hasPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPathHelper(v1,v2,visited)

g = Graph(6)
g.addEdge(5,3)
g.addEdge(0,1)
g.addEdge(3,4)

print(g.hasPath(0,3))
