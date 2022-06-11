import pandas as pd
import csv
import numpy as np
class Knapsack:

    def __init__(self, items, values, costs, B):
        self.items = items
        self.values = values
        self.costs = costs
        self.B = B
        self.vc = []
        self.len = len(self.items)
        for i in range(len(self.items)):
            self.vc.append(self.values[i]/self.costs[i])

    def write_to_file(self):
        with open('../Files/KnapsackInstances.csv', 'a+') as f:
            writer = csv.writer(f)
            writer.writerow([self.items, self.values, self.costs, self.B])


    def print(self):
        print('Items: ', self.items)
        print('Values: ', self.values)
        print('Costs: ', self.costs)
        print('Budget: ', self.B)
        print('Value/Cost: ', self.vc)

#GREEDY HELPER FUNCTIONS
    def swap(self, a, b):
        temp_vc, temp_val, temp_cost, temp_items = self.vc[a], self.values[a], self.costs[a], self.items[a]
        self.vc[a], self.values[a], self.costs[a], self.items[a] = self.vc[b], self.values[b], self.costs[b], self.items[b]
        self.vc[b], self.values[b], self.costs[b], self.items[b] = temp_vc, temp_val, temp_cost, temp_items

    def partition(self, start, end):
        pivot = self.vc[end]
        lastLeft = start - 1
        firstUnknown = start
        while firstUnknown < end:
            if self.vc[firstUnknown] < pivot:
                lastLeft += 1
                self.swap(lastLeft, firstUnknown)
            firstUnknown += 1
        self.swap(lastLeft + 1, end)
        return lastLeft+1

    def quickSort(self, start, end):
        if start < end:
            pivotIndex = self.partition(start, end)
            self.quickSort(start, pivotIndex-1)
            self.quickSort(pivotIndex + 1, end)

    def max_val(self):
        max_index = 0
        max_val = 0
        for i in range(len(self.items)):
            if self.values[i] > max_val:
                max_index, max_val = i, self.values[i]

        return max_index

    def reverse(self):
        self.vc.reverse(), self.values.reverse(), self.costs.reverse(), self.items.reverse()


#MINCOST HELPER
    def mincost_Soln(self, MinCost, n, aMax):
        maxindex = 0
        for i in range(n*aMax):
            if MinCost[n, i] <= self.B:
                maxindex = i
        return maxindex

