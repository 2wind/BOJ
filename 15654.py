import itertools

N, M = [int(x) for x in input().split()]
n_list = sorted([int(x) for x in input().split()])
# _N C_M

def from_select(n_list, r):
    result = []
    if r == 1:
        result = n_list
    else:
        for i in range(len(n_list)):
            list_slice = n_list[i:]
            low_level = from_select(list_slice, r-1)
            for j in range(len(low_level)):
                result.append([n_list[i], low_level[j]])
    return result

def flatten_recursive(element):
    if type(element) != list:
        return str(element)
    
    else:
        return " ".join([flatten_recursive(x) for x in element])

combi = from_select(n_list, M)
for k in range(len(combi)):
    #print(combi[k])
    print(flatten_recursive(combi[k]))

