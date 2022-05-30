from collections import deque

def times2(x):
    return 2 * x

def concat1(x):
    return 10 * x + 1


A, B = [int(x) for x in input().split()]


DQ = deque()
DQ.append((A, 0))

solution_found = False
while DQ:
    number, count = DQ.popleft()

    if count > 0 and number == B:
        solution_found = True
        break

    if number > B:
        continue
    
    DQ.append((times2(number), count+1))
    DQ.append((concat1(number), count+1))


print(count + 1) if solution_found else print(-1)
