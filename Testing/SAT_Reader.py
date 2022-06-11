import csv
from Objects.SAT import SAT

def clean_instance(instance):
    new_instance = []

    instance = instance.split('],')
    for clause in instance:

        clause = clause.strip('[[')
        clause = clause.strip(']]')
        clause = clause.strip(', [')
        clause = clause.split(',')
        new_instance.append(list(map(int, clause)))

    return new_instance




def read_instances():
    with open('../Files/SATInstances.csv', 'r') as f:
        reader = csv.reader(f)
        sat = []
        for row in reader:
            sat.append(SAT(clean_instance(row[0])))

    return sat