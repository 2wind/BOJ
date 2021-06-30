import sys
from collections import deque

N, K = [int(x) for x in input().split()]

weights = deque()
table = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(N):
    weight, value = [int(x) for x in sys.stdin.readline().strip().split()]
    weights.append((weight, value))

for i in range(1, N+1):
    weight, value = weights[i-1]

    for j in range(1, K+1):
        if weight <= j:
            table[i][j] = max(table[i-1][j], value + table[i-1][j-weight])
        else:
            table[i][j] = table[i-1][j]

print(table[N][K])
