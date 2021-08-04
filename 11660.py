from collections import deque
import sys

N, M = [int(x) for x in input().split()]

matrix = [[0 for j in range(N+1)] for i in range(N+1)]
sums = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(N):
    line = [int(x) for x in sys.stdin.readline().strip().split()]
    for j in range(N):
        matrix[i+1][j+1] = line[j]

questions = deque()

for i in range(M):
    questions.append([int(x) for x in sys.stdin.readline().strip().split()])

for i in range(1,N+1):
    for j in range(1,N+1):
        sums[i][j] = -sums[i-1][j-1] + sums[i-1][j] + sums[i][j-1] + matrix[i][j]



# print(matrix)
# print(questions)
# print(sums)

for question in questions:
    x1, y1, x2, y2 = question
    
    print(sums[x2][y2] - sums[x2][y1-1] - sums[x1-1][y2] + sums[x1-1][y1-1])