import numpy as np


def nW(K):
    F = np.zeros([K.len+1, K.B+1])
    n = K.len
    for i in range(n-1, -1, -1):
        for w in range(K.B+1):
            if K.costs[i] <= w:
                F[i,w] = max(F[i+1, w-K.costs[i]] + K.values[i], F[i+1, w])
            else:
                F[i,w] = F[i+1, w]

    return F[0,K.B]
