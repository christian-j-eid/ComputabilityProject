import numpy as np




def minCost(K):
    aMax = max(K.values)
    n = K.len
    MinCost = np.zeros([n+1, n*n*aMax+1])

    for t in range(0, K.values[0]+1):
        MinCost[0, t] = K.costs[0]

    for t in range(K.values[0]+1, n*aMax +1):
        MinCost[0, t] = np.infty

    for i in range(1, n):
        for t in range(0, n*aMax + 1):
            NextT = max(0, t-K.values[i])
            if MinCost[i-1, t] <= K.costs[i] + MinCost[i-1, NextT]:
                MinCost[i, t] = MinCost[i-1, t]
            else:
                MinCost[i, t] = K.costs[i] + MinCost[i-1, NextT]

    return K.mincost_Soln(MinCost, n-1, aMax)



