"""
Vertices : Vertices are the nodes of the graph
Edge : Edge is the line that connects pair of vertices
Unwieghted Graph : A graph which does not have weight associated with any edge
Weighted Graph : A graph which has weight associated with any edge
Undirect Graph : In case the edges of the graph do not have a direction associated with them
Directed Graph : If the edges in a graph have a direction associated with them
Cyclic Graph : A graph which has at least one loop
Acylic Graph : A graph whith no loop
Tree : Tree is a special case of directed acyclic graph

Graph Types:
                            Graph
                        /            \
                Directed             Undirected
                /    \                  /    \
        Weighted    Unweighted    Weighted    Unweighted 
        /    \                    /    \
Positive    Negative         Positive   Negative

If a graph is complete or almost complete we should use Adjacency Matrix
If the number of edges are few then we should use Adjacency List
"""

"""
      Timecomplexity   Spacecomplexity
bfs   O(V+E)           O(V)
dfs   O(V+E)           O(V)
"""

from queue import Queue, LifoQueue

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
        return "Vertex added successfully"

    def add_edge(self, vertex1, vertex2):
        vertices = self.adjacency_list.keys()
        if vertex1 in vertices and vertex2 in vertices:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        return "Edge added successfully"

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
        return "Vertex removed successfully"
    
    def remove_edge(self, vertex1, vertex2):
        vertices = self.adjacency_list.keys()
        if vertex1 in vertices and vertex2 in vertices:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
        return "Edge removed successfully"
    
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        q = Queue()
        q.put(vertex)
        while not q.empty():
            current_vertex = q.get()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    q.put(adjacent_vertex)
    
    def dfs(self, vertex):
        visited = set()
        stack = LifoQueue()
        stack.put(vertex)
        while not stack.empty():
            current_vertex = stack.get()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.put(adjacent_vertex)

    def print_graph(self):
        for tpl in self.adjacency_list.items():
            print(tpl)

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "E")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.print_grapth()
graph.bfs("A")
graph.dfs("A")
