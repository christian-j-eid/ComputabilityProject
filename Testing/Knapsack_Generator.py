from Objects.Knapsack import Knapsack
import random

#RANDOM KNAPSACK INSTANCE GENERATION


def generate_knapsack_sample():
    item_count = random.randint(10, 100)

    itemSet = []
    valueSet = []
    costSet = []
    B = random.randint(1, 5000)
    for i in range(item_count):
        itemSet.append(str(i))
        valueSet.append(random.randint(1, 1000))
        costSet.append(random.randint(1, 1000))


    K = Knapsack(itemSet, valueSet, costSet, B)
    K.write_to_file()

for i in range(100):
    generate_knapsack_sample()