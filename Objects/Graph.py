import networkx as nx
import matplotlib.pyplot as plt
import tsplib95 as tsp




class Graph:
    def __init__(self, filepath):
        problem = tsp.load(filepath)
        self.problem = problem
        self.G = problem.get_graph()
        self.nodes = self.G.nodes
        self.edges = self.G.edges

    def trace_tour(self, tour):
        return self.problem.trace_tours(tour)
    def print(self):
        print("Graph: ", self.G)
        print("Nodes: ", self.nodes)
        print("Edges: ", self.edges)




    def draw(self):

        pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx(self.G, pos)
        nx.draw_networkx_edge_labels(self.G,pos, edge_labels=labels)
        plt.show()

