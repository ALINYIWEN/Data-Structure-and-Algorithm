# Adjacency Matrix representation 

class Graph:
    # Initialize the matrix
    def __init__(self, size):
        self.adj_Matrix = []
        for i in range(size):
            self.adj_Matrix.append([0 for i in range(size)])
        self.size = size    

    # add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d"%(v1, v2))
        self.adj_Matrix[v1][v2] = 1
        self.adj_Matrix[v2][v1] = 1

    # remove edges
    def remove_edges(self, v1, v2):
        if self.adj_Matrix[v1][v2] == 0:
            print("No edges between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    # Print the matrix
    def print_matrix(self):
        for row in self.adj_Matrix:
            for val in row:
                print('{:4}'.format(val)),
            print
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_matrix()