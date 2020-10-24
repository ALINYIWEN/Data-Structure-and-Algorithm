# Adjascency List representation

class Adj_Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.v = num
        self.graph = [None] * self.v

    # Add edges
    def add_edge(self, s, d):
        node = Adj_Node(d)
        node.next = self.graph[s]            
        self.graph[s] = node

        node = Adj_Node(s)
        node.next = self.graph[d]            
        self.graph[d] = node

    # print the graph
    def print_graph(self):
        for i in range(self.v):
            print("vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")



V = 5
# Create graph and edges
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

graph.print_graph()
