import sys
from collections import deque


N = int(input())

pyramid = deque()
record = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    pyramid.append([int(x) for x in sys.stdin.readline().strip().split()])


for i in range(0,N):
    for j in range(0,i+1):
        if i == 0:
            record[i][j] = pyramid[i][j]
        elif j == 0:
            record[i][j] = record[i-1][j] + pyramid[i][j]
        elif i == j:
            record[i][j] = record[i-1][j-1] + pyramid[i][j]
        else:
            record[i][j] = max(record[i-1][j], record[i-1][j-1]) + pyramid[i][j]

print(max(record[N-1]))