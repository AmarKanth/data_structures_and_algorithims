"""
Sorts given actions in such a way that if there is a dependency of one action on another, 
then the dependent action always comes later than its parent action
"""
from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for adjacent_vertex in self.graph[vertex]:
            if adjacent_vertex not in visited:
                self.topologicalSortUtil(adjacent_vertex, visited, stack)
        
        stack.insert(0, vertex)
    
    """
    TimeComplexity is O(V+E)
    SpaceComplexity is O(V+E)
    """
    def topologicalSort(self):
        visited = []
        stack = []

        for vertex in list(self.graph):
            if vertex not in visited:
                self.topologicalSortUtil(vertex, visited, stack)
        
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A","C")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge("B","D")
customGraph.addEdge("B","C")
customGraph.addEdge("D","F")
customGraph.topologicalSort()