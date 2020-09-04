import itertools

N, M = [int(x) for x in input().split()]

# _N C_M

def from_select(n_list, r):
    result = []
    if r == 1:
        result.append(n_list)
    else:
        for i in range(len(n_list)-1):
            low_level = from_select(n_list[i+1:], r-1)
            for j in range(len(low_level)):
                result.append([n_list[i], low_level[j]])
    return result

def flatten_recursive(element):
    if type(element) != list:
        return element
    
    else:
        return " ".join(element)

combi = from_select([str(x) for x in range(1, N+1)], M)
print(len(combi))
for k in range(len(combi)):
    print(combi[k])

