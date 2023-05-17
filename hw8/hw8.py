import sys

def knapsack(items, capacity):
    """
    dp solution to knapsack problems in O(nW) time complexity
    input: items- list of items which is a list with [weight, value], capacity - maximum wieght
    return: maximum possible value from the list of items.
    """
    # 2d DP Matrix, row - items, column - capacity. M[i][j] = maximum value for first i items and j capacity
    M = [ [0]*(capacity + 1) for i in range(len(items)+1)]

    # Apply DP algorithm by populate matrix for each row and column other than row0 and column 0 - which is all 0(base case)
    for i in range(1,len(M)):
        for w in range(1, len(M[i])):
            # Bellman Equation from lecture
            ind = 0 if items[i-1][0] > w else 1
            if ind == 0:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1] [w], ind * (M[i-1][w - items[i-1][0]] + items[i-1][1]))
    
    # solution is store at M[n, W]
    return int(M[len(items)][capacity]) 

if __name__ == '__main__': 
    # process input here
    num_instance = int(sys.stdin.readline())
    result = [] # store all result

    # readin data
    for i in range(num_instance):
        item_capacity = list(map(int, sys.stdin.readline().strip().split()))
        item_num = item_capacity[0]
        capacity = item_capacity[1]
        items = []
        for i in range(item_num):
            items.append(list(map(int, sys.stdin.readline().strip().split())))
        result.append(knapsack(items, capacity))
    
    # print all results
    for res in result:
        sys.stdout.write(str(res) + '\n')