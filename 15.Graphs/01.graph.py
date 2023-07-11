from queue import Queue, LifoQueue

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def print_grapth(self):
        for key, val in self.adjacency_list.items():
            print(key,":",val)
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    
    """
    TimeComplexity is O(V+E)
    SpaceComplexity is O(V)
    """
    def bfs(self, vertex):
        # It works similar way as levelorder-traversal
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
    
    """
    TimeComplexity is O(V+E)
    SpaceComplexity is O(V)
    """
    def dfs(self, vertex):
        # It goes top to deepest-node and deepest-node to top
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


custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")
custom_graph.add_edge("A", "B")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "E")
custom_graph.add_edge("C", "D")
custom_graph.add_edge("D", "E")
custom_graph.print_grapth()
# custom_graph.bfs("A")
custom_graph.dfs("A")