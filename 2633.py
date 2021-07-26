import sys
from collections import deque
import heapq

class Node():
    def __init__(self, n):
        self.number = n
        self.linkfrom = []
        self.linkto = []
        self.fromcount = 0

    def __gt__(self, value):
        if self.fromcount == value.fromcount:
            return self.number > value.number

        else:
            return self.fromcount > value.fromcount
        
    def __str__(self):
        return str(self.number)


N, M = [int(x) for x in sys.stdin.readline().split()]
students = [Node(int(x)) for x in range(N+1)]
students[0].fromcount = -1

for i in range(M):
    line = [int(x) for x in sys.stdin.readline().split()]
    for i in range(1, len(line)-1):
        X, Y = line[i], line[i+1]
        students[X].linkto.append(students[Y])
        students[Y].linkfrom.append(students[X])
        students[Y].fromcount += 1


disQ = []
resultQ = deque()

tpsort = deque()

for s in students:
    if s.fromcount == 0:
        heapq.heappush(disQ, (s.fromcount, s))

while disQ:
    fromcount, node = heapq.heappop(disQ)
    tpsort.append(node)
    for child in node.linkto:
        child.fromcount -= 1
        if child.fromcount == 0:
            heapq.heappush(disQ, (child.fromcount, child))

if len(tpsort) == N:
    print("\n".join(map(str, tpsort)))
else:
    print("0")
        

    