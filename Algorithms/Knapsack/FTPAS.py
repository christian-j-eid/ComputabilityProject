import math
from Algorithms.Knapsack.mincost import minCost
from Objects.Knapsack import Knapsack

def FTPAS(K, F):
    items = K.items
    values = K.values
    scaled_values = []
    costs = K.costs
    B = K.B

    for i in range(K.len):
        scaled_values.append(math.floor(values[i]/F))
    K = Knapsack(items, scaled_values, costs, B)


    return minCost(K)
