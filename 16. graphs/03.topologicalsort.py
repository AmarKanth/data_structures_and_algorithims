"""
Sorts given actions in such a way that if there is a dependency of one action on another, 
then the dependent action always comes later than its parent action
"""
from collections import defaultdict

class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)

        for adjacent_vertex in self.graph[vertex]:
            if adjacent_vertex not in visited:
                self.topological_sort_util(adjacent_vertex, visited, stack)
        
        stack.insert(0, vertex)
    
    """
    TimeComplexity is O(V+E)
    SpaceComplexity is O(V+E)
    """
    def topological_sort(self):
        visited = []
        stack = []

        for vertex in list(self.graph):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)
        
        print(stack)

graph = Graph(8)
graph.add_edge("A","C")
graph.add_edge("C","E")
graph.add_edge("E","H")
graph.add_edge("E","F")
graph.add_edge("F","G")
graph.add_edge("B","D")
graph.add_edge("B","C")
graph.add_edge("D","F")
graph.topological_sort()
