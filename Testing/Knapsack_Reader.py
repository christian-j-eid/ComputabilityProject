import csv
from Objects.Knapsack import Knapsack

def clean_items(items):
    items = items.strip('[')
    items = items.strip(']')
    items = items.replace('\'', '')
    items = items.replace(' ', '')
    return items.split(',')

def clean_ints(string):
    lst = clean_items(string)
    return list(map(int, lst))

def get_knapsack(row):
    items = clean_items(row[0])
    values = clean_ints(row[1])
    costs = clean_ints(row[2])
    B = int(row[3])
    return Knapsack(items, values, costs, B)


def read_instances():
    with open('../Files/KnapsackInstances.csv', 'r') as f:
        reader = csv.reader(f)
        knapsacks = []
        for row in reader:
            knapsacks.append(get_knapsack(row))
    return knapsacks


