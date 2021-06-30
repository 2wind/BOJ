import sys
from collections import deque

def distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

def get_min_chicken(distances, queue):
    sum = 0
    for home in range(len(distances)):
        min = 1000000
        for i in queue:
            if distances[home][i] < min:
                min = distances[home][i]
        sum += min
    return sum

N, M = [int(x) for x in input().split()]

city = [[0 for i in range(N)] for j in range(N)]
houses = deque()
chickens = deque()

for i in range(N):
    city[i] = [int(x) for x in sys.stdin.readline().strip().split()]
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))

distances = [[0 for i in range(len(chickens))] for j in range(len(houses))]
# [houses, chickens]

for i in range(len(houses)):
    for j in range(len(chickens)):
        distances[i][j] = distance(houses[i], chickens[j])

queue = list(range(0, M))
mins = deque()


def check_and_increment(C, queue, M, i, minimums):
    
    minimums.append(get_min_chicken(distances, queue))
    if i >= 0:
        CMI = C - M + i
        if queue[i] < CMI :
            # print(queue)
            queue[i] += 1
            check_and_increment(C, queue, M, i, minimums)
        else:
            check_and_increment(C, queue, M, i-1, minimums)
            queue[i] = queue[i-1] + 1

    

for i in range(1, M+1):
    m = deque()
    check_and_increment(len(chickens), queue, i, i-1, m)
    mins.append(min(m))
print(min(mins))