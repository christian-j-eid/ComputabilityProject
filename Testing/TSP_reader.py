from Objects.Graph import Graph
import tsplib95 as tsp

def read(file, tour):
    G = Graph(file)
    OPT = tsp.load(tour)
    return G, OPT
