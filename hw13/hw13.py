import sys
import random
import math

def rand_assign(num_variable):
    """
    Generate a random assignment for all possible variables
    """
    # dictionary to store assignment
    assignment_dict = {}
    for i in range(1, num_variable + 1):
        # generate random number between 1 and 10, if 1-5, assign 0, else assign 1
        rand_num = random.randint(1, 10)
        assignment_dict[i] = 1 if rand_num > 5 else 0
    return assignment_dict


def random_max_3sat(clauses_list, num_variable, num_clause):
    """
    Get random assignment and evaluate to find an assignment that satisfies at least 7/8 of the clauses
    """
    final_assignment = None
    while(True):
        satisfied = 0
        assignment = rand_assign(num_variable)
        # evaluate assignment
        for clause in clauses_list:
            x1 = clause[0]
            x2 = clause[1]
            x3 = clause[2]
            val1 = assignment[x1] if x1 > 0 else 1 - assignment[-x1]
            val2 = assignment[x2] if x2 > 0 else 1 - assignment[-x2]
            val3 = assignment[x3] if x3 > 0 else 1 - assignment[-x3]
            if val1 == 1 or val2 == 1 or val3 == 1:
                satisfied += 1
        # if satisfied >= 7/8 of the clauses, break
        if satisfied >= math.floor((7/8) * num_clause):
            final_assignment = assignment
            break
    # convert assignment to a result list for printing
    assign_list = []
    for i in range(1, num_variable + 1):
        if final_assignment[i] == 1:
            assign_list.append(1)
        else:
            assign_list.append(-1)
    return assign_list

        
if __name__ == '__main__': 
    # process input here
    num_variable = int(sys.stdin.readline())
    num_clause = int(sys.stdin.readline())

    clauses_list = [] # store all clauses
    # readin data
    for i in range(num_clause):
        clause = sys.stdin.readline().strip().split()
        clause = [int(x) for x in clause]
        clauses_list.append(clause)
    
    # call random_max_3sat to get assignment and print result
    result = random_max_3sat(clauses_list, num_variable, num_clause)
    for res in result:
        print(res, end=' ')