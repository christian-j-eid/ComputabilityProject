from Algorithms.TSP.Kruskal import Kruskal
from Objects.Node import Node

global tour_cost
tour_cost = 0
def MinTSP(graph):

    MST, A = Kruskal(graph)
    root = 1

    i = 0
    while len(MST) != 0:
        i += 1
        walk(graph, MST, MST[0][0])

    global tour_cost
    print('MST tour walking', 2*tour_cost)
    tour_cost = 0

def walk(graph, MST, root):

    for edge in MST:
        if root in edge:
            global tour_cost
            tour_cost += graph.edges[edge]['weight']
            MST.remove(edge)
            if root == edge[0]:
                walk(graph, MST, edge[1])
            else:
                walk(graph, MST, edge[0])

def walk_save(graph, MST, root):

    for edge in MST:
        if root in edge:
            weight = graph.edges[edge]['weight']
            tour_cost += weight
            MST.remove(edge)
            if root == edge[0]:
                return weight + walk(graph, MST, edge[1])
            else:
                return weight + walk(graph, MST, edge[0])

    return 0

