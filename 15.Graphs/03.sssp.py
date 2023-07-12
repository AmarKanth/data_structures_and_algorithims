from queue import Queue

"""
Breadth First Search
"""
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def print_graph(self):
        for vertex, edges in self.gdict.items():
            print(vertex,":",edges)
    
    """
    Note : It visits only connected nodes
    TimeComplexity: O(E)
    SpaceComplexity: O(E)
    """
    def bfs(self, start, end):
        q = Queue()
        q.put([start])
        while not q.empty():
            path = q.get()
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                q.put(new_path)

# If we change the order of edges in vertex shortest path will change
customDict = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "G": ["F"]
}

graph = Graph(customDict)
print(graph.print_graph())
print(graph.bfs("A", "F"))