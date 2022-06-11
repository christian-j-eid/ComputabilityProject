import random
from Objects.SAT import SAT
def generate_SAT():

    number_of_clauses = random.randint(300, 400)
    literal_range =  random.randint(100, 150)

    instance = []

    for i in range(number_of_clauses):
        values_in_clause = []
        clause = []
        while len(clause) < 3:
            literal = random.randint(-literal_range, literal_range)
            if literal not in values_in_clause and literal != 0:
                clause.append(literal)
                values_in_clause.append(literal)
        if clause not in instance:
            instance.append(clause)


    return instance

for i in range(100):
    sat = SAT(generate_SAT())
    sat.write_to_file()