from Objects.SAT import SAT
from copy import deepcopy



def isEmpty(formula):
    if len(formula) == 0:
        return True
    return False

def containsEmptyClause(formula):
    for clause in formula:
        if len(clause) == 0:
            return True
    return False

def containsUnit(formula):
    for i in range(len(formula)):
        if len(formula[i]) == 1:
            if i == 0:
                return -2
            return i
    return False

def containsxj(formula, xj):
    for clause in formula:
        for literal in clause:
            if literal == xj:
                return True
    return False

def remove_clause(formula, xj):
    for clause in formula:
        for literal in clause:
            if literal == xj:
                formula.remove(clause)
    if containsxj(formula, xj):
        remove_clause(formula, xj)

def remove_xj(formula, xj):
    for clause in formula:
        for literal in clause:
            if literal == xj:
                clause.remove(xj)

def UnitPropogation(formula, truthAssignmentSoFar):
    contains_unit = containsUnit(formula)

    zero_workaround = False
    if contains_unit == -2:
        zero_workaround = True

    while contains_unit or zero_workaround:

        if zero_workaround:
            xj = formula[0][0]

            zero_workaround = False
        else:

            xj = formula[contains_unit][0]

        if xj > 0:
            truthAssignmentSoFar[xj] = True
            remove_clause(formula, xj)
            remove_xj(formula, -xj)

        else:
            truthAssignmentSoFar[-xj] = False
            remove_clause(formula, xj)
            remove_xj(formula, -xj)
        contains_unit = containsUnit(formula)
        if contains_unit == -2:
            zero_workaround = True

    return truthAssignmentSoFar, formula

def DPLL(formulaSoFar, truthAssignmentSoFar):
    newAssignment, newFormula = UnitPropogation(formulaSoFar, truthAssignmentSoFar)
    # sat = deepcopy(sat1)
    # sat.formula = newFormula
    # sat.assignment = newAssignment
    # sat.print_dpll()
    if isEmpty(newFormula):
        # print("SATISFIABLE WITH: ", newAssignment)
        return True, newAssignment
    if containsEmptyClause(newFormula):
        # print("Unsatisfiable leaf w: ", newAssignment)
        return False

    xi = newFormula[0][0]

    newFormula.append([xi])
    newAssignment[xi] = True

    result = DPLL(deepcopy(newFormula), newAssignment)

    if result:
        return True, newAssignment
    else:
        not_xi = -newFormula[0][0]

        newFormula.append([not_xi])
        newAssignment[-not_xi] = False
        return DPLL(newFormula, newAssignment)

def start_DPLL(SAT):
    f = SAT.formula
    a = SAT.assignment
    return DPLL(f, a)

