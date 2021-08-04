import heapq
from collections import deque
import sys

class Node():
    def __init__(self, n):
        self.n = n
        self.visited = False
        self.edges = deque()

    def __str__(self):
        return str(self.n)



V, E = [int(x) for x in input().split()]

nodes = [Node(i) for i in range(V+1)]

edgeQ = []

for i in range(E):
    A, B, C = [int(x) for x in sys.stdin.readline().strip().split()]
    edge1 = (C, A, B)
    edge2 = (C, B, A)
    nodes[A].edges.append(edge1)
    nodes[B].edges.append(edge2)


visit = 1
current = nodes[1]
current.visited = True
weight = 0
while visit < V:
    # print(visit)
    # print(edgeQ)
    # print(current)
    
    for edge in current.edges:
        if not nodes[edge[2]].visited:
            heapq.heappush(edgeQ, edge)
    while edgeQ:
        selected = heapq.heappop(edgeQ)
        if not nodes[selected[2]].visited:
            break
    
    # print(selected)
    # print("---------")
    weight += selected[0]
    current = nodes[selected[2]]
    current.visited = True
    visit += 1

print(weight)