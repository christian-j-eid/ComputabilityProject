import random
def GSAT(sat):

    sat.getAllVar()
    for val in sat.assignment:
        if random.randint(0, 1) == 1:
            sat.assignment[val] = True
        else:
            sat.assignment[val] = False

    starting_val = sat.checkSuccess()

    # sat.print_dpll()

    best_candidate = sat.local_search()
    iteration = 0
    while best_candidate != 0:
        iteration += 1
        sat.assignment[best_candidate] = not sat.assignment[best_candidate]
        best_candidate = sat.local_search()

    # print("GSAT finished in ", iteration, "iterations with a success of ", sat.checkSuccess())
    return sat
