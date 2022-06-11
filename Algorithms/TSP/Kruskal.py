from Objects.Graph import Graph
from Objects.DisjointSet import DisjointSetForest
import csv

#
def Kruskal(graph):
    A = []
    ds = DisjointSetForest()

    for vertex in graph.nodes:
        ds.makeSet(vertex)
    count = 0
    edges = []
    weights = []
    for i in range(1, len(graph.nodes) + 1):
        for j in range(i, len(graph.nodes) + 1):
            edges.append((i, j))
            weights.append(graph.edges[i, j]['weight'])
            count += 1

    quickSort(edges, weights, 0, len(edges)-1)

    for edge in edges:
        u = edge[0]
        v = edge[1]
        if ds.findSet(u) != ds.findSet(v):
            A.append((u, v))
            ds.union(u, v)

    return A, ds



def swap(edges, weights, a, b):
    temp_edge, temp_weight = edges[a], weights[a]
    edges[a], weights[a] = edges[b], weights[b]
    edges[b], weights[b] = temp_edge, temp_weight


def partition(edges, weights, start, end):
    pivot = weights[end]
    lastLeft = start - 1
    firstUnknown = start
    while firstUnknown < end:
        if weights[firstUnknown] < pivot:
            lastLeft += 1
            swap(edges, weights, lastLeft, firstUnknown)
        firstUnknown += 1
    swap(edges, weights, lastLeft + 1, end)
    return lastLeft+1

def quickSort(edges, weights, start, end):
    if start < end:
        pivotIndex = partition(edges, weights, start, end)
        quickSort(edges, weights, start, pivotIndex-1)
        quickSort(edges, weights, pivotIndex + 1, end)