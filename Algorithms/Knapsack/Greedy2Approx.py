
#Greedy 2-Approx Algorithm

def Greedy_2_Approximation(K):
    #Sorting by Value/Cost

    K.quickSort(0, K.len-1)
    K.reverse()

    curr_budget, max_Val, i = 0, 0, 0
    items_taken = []
    at_capacity = False

    while not at_capacity:
        if i >= K.len:

            return max_Val
        if curr_budget + K.costs[i] < K.B:
            curr_budget += K.costs[i]
            max_Val += K.values[i]
            items_taken += K.items[i]
            i += 1
        else:
            at_capacity = True

    v_max = K.max_val()
    if max_Val < K.values[v_max]:
        max_Val = K.values[v_max]
        items_taken = K.items[v_max]
        curr_budget = K.costs[v_max]

    return max_Val

    print('Items sorted by v/c: ', K.items)
    print('Value and Cost:', K.values, K.costs)
    print('Items taken: ', items_taken)
    print('MaxVal: ', max_Val)
    print('remaining budget', K.B-curr_budget)
