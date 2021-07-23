import sys
from collections import deque

N, M = [int(x) for x in input().split()]

table = [[0 for i in range(10)] for j in range(N+1)]

mems = [int(x) for x in sys.stdin.readline().strip().split()]
costs = [int(x) for x in sys.stdin.readline().strip().split()]
table = [[0 for i in range(sum(costs)+1)] for j in range(N+1)]

min_index = sys.maxsize

if N == 1:
    print(costs[0])

else:
    for i in range(1, N+1):
        mem, cost = mems[i-1], costs[i-1]

        for j in range(len(table[0])):
            if cost <= j:
                table[i][j] = max(table[i-1][j], mem + table[i-1][j-cost])

            else:
                table[i][j] = table[i-1][j]
            if table[i][j] >= M and j < min_index:
                min_index = j
    print(min_index)
