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
