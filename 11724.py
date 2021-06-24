n, m = [int(x) for x in input().split()]

arr = {}

# print(arr)
num = 0

def visit(elem):
    if elem[0]:
        return
    elem[0] = True
    for i in elem[1]:
        visit(arr[i])        

def select_min():
    for i in arr.keys():
        if arr[i][0] == False:
            return i
    return None


for i in range(m):
    p, q = [int(x) for x in input().split()]
    if (p in arr.keys()):
        arr[p][1].append(q)
    else:
        arr[p] = [False, [q]]
    if (q in arr.keys()):
        arr[q][1].append(p)
    else:
        arr[q] = [False, [p]]
    

if len(arr.keys()) < n:
    for i in range(1001, 1001 + n - len(arr.keys())):
        arr[i] = [False, []]

while True:
    i = select_min()
    if i is None:
        break

    num = num + 1
    visit(arr[i])

print(num)
