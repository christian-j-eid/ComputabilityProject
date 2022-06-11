from copy import deepcopy
import csv
class SAT:

    def __init__(self, instance):
        self.instance = instance #Maintains original instance
        self.formula = deepcopy(instance) #Can be modified for use
        self.assignment = {}
        self.SATISFIABLE = False

    #DPLL Helper

    def isEmpty(self):
        if len(self.formula)==0:
            return True
        return False

    def containsEmptyClause(self):
        for clause in self.formula:
            if len(clause) == 0:
                return True
        return False

    def containsUnit(self):
        for i in range(len(self.formula)):
            if len(self.formula[i])==1:
                return i
        return False

    def containsxj(self, xj):
        for clause in self.formula:
            for literal in clause:
                if literal == xj:
                    return True
        return False

    def remove_clause(self, xj):
        for clause in self.formula:
            for literal in clause:
                if literal == xj:
                    self.formula.remove(clause)
        if self.containsxj(xj):
            self.remove_clause(xj)

    def remove_xj(self, xj):
        for clause in self.formula:
            for literal in clause:
                if literal == xj:
                    clause.remove(xj)
                    # if len(clause)==0:
                    #     self.formula.remove(clause)

    def print_dpll(self):
        print('Original Instance: ', self.instance)
        print('formula: ', self.formula)
        print('Assignment: ', self.assignment)


    #Randomized Helper

    def check_truth(self):
        clause_truths = []
        for clause in self.instance:
            clause_truths.append(self.check_clause(clause))
        return clause_truths

    def check_clause(self, clause):
        for literal in clause:
            if literal > 0:
                if self.assignment[literal] == True:
                    return True
            if literal < 0:
                if self.assignment[-literal] == False:
                    return True
        return False

    def checkSuccess(self):
        outcome = self.check_truth()
        success_rate = 0
        for val in outcome:
            if val:
                success_rate += 1
        success = success_rate / len(outcome)
        return success

    def getAllVar(self):
        for clause in self.instance:
            for literal in clause:
                if literal > 0:
                    self.assignment[literal] = 0
                else:
                    self.assignment[-literal] = 0


    #GSAT HELPERS

    def local_search(self):

        best_candidate = 0
        curr_success = self.checkSuccess()

        for literal in self.assignment:

            temp_sat = SAT(self.instance)
            temp_sat.assignment = deepcopy(self.assignment)
            temp_sat.assignment[literal] = not temp_sat.assignment[literal]
            # print('Success for flipping x[',literal,']: ', temp_sat.checkSuccess())
            if temp_sat.checkSuccess() > curr_success:

                curr_success = temp_sat.checkSuccess()
                best_candidate = literal

        # print('Best candidate : ', best_candidate)
        return best_candidate


    def write_to_file(self):
        with open('../Files/SATInstances.csv', 'a+') as f:
            writer = csv.writer(f)
            writer.writerow([self.instance])
