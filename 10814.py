import sys
from collections import deque

N = int(input())

q = deque()

for i in range(N):
    line = sys.stdin.readline().strip().split()
    age, name = int(line[0]), line[1]
    q.append((i, age, name))

ls = list(q)
ls.sort(key = lambda x: x[0])
ls.sort(key = lambda x: x[1])

for i in ls:
    sys.stdout.write(str(i[1]) + " " + i[2] + "\n")

