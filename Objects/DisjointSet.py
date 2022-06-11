
#Class DisjointSetForest is based off of pseudocode from CLRS page 571


class DisjointSetForest:

    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def makeSet(self, x):
        self.parents[x] = x
        self.ranks[x] = 0

    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.ranks[x] > self.ranks[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.ranks[x] == self.ranks[y]:
                self.ranks[y]+=1

    def findSet(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.findSet(self.parents[x])
        return self.parents[x]

    def print(self):
        print('PARENTS: ',self.parents)
        print('RANKS: ',self.ranks)
