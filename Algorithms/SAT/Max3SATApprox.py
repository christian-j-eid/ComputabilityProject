from Objects.SAT import SAT
import random

def Approx(sat):
    sat.getAllVar()
    # sat.print_dpll()
    for val in sat.assignment:
        if random.randint(0, 1) == 1:
            sat.assignment[val] = True
        else:
            sat.assignment[val] = False
    # sat.print_dpll()
    #
    # print(sat.checkSuccess())
    return sat

