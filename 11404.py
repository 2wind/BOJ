import sys
import math
from collections import deque

n = int(input())
m = int(input())

adj = [[math.inf for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    adj[i][i] = 0
for i in range(m):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    if adj[a][b] > c:
        adj[a][b] = c



for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])


for i in range(1, n+1):
    print(" ".join([str(x) for x in adj[i][1:]]))