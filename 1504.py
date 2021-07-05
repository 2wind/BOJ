import sys
import math
from collections import deque
import heapq


class Node():
    def __init__(self, number):
        self.number = number
        self.edges = []
        self.distance = math.inf

    def __str__(self):
        if math.isinf(self.distance):
            return "INF"
        else:
            return f"{self.distance}"

    def __gt__(self, other):
        if self.distance != other.distance:
            return self.distance > other.distance
        else:
            return self.number > other.number

    def __eq__(self, other):
        if self.distance != other.distance:
            return False
        else:
            return self.number == other.number



V, E = [int(x) for x in input().split()] # Vertices, Edges
# node 1 --> V

adj1 = [Node(x) for x in range(V+1)]
adj2 = [Node(x) for x in range(V+1)]
adj3 = [Node(x) for x in range(V+1)]

for i in range(E):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    adj1[a].edges.append((a, b, c))
    adj1[b].edges.append((b, a, c))
    adj2[a].edges.append((a, b, c))
    adj2[b].edges.append((b, a, c))
    adj3[a].edges.append((a, b, c))
    adj3[b].edges.append((b, a, c))

v1, v2 = [int(x) for x in input().split()]

adj1[1].visited = True
adj1[1].distance = 0
adj2[v1].visited = True
adj2[v1].distance = 0
adj3[v2].visited = True
adj3[v2].distance = 0


q1 = []
q2 = []
q3 = []

for node in adj1[1:]:
    heapq.heappush(q1, (node.distance, node))

for node in adj2[1:]:
    heapq.heappush(q2, (node.distance, node))

for node in adj3[1:]:
    heapq.heappush(q3, (node.distance, node))

while len(q1) > 0:
    curr = heapq.heappop(q1)
    if curr[0] >= curr[1].distance:
        for edge in curr[1].edges:
            dist_now = adj1[edge[1]].distance
            adj1[edge[1]].distance = min(adj1[edge[1]].distance, curr[1].distance + edge[2])
            if adj1[edge[1]].distance < dist_now:
                heapq.heappush(q1, (adj1[edge[1]].distance, adj1[edge[1]]))
        
while len(q2) > 0:
    curr = heapq.heappop(q2)
    if curr[0] >= curr[1].distance:
        for edge in curr[1].edges:
            dist_now = adj2[edge[1]].distance
            adj2[edge[1]].distance = min(adj2[edge[1]].distance, curr[1].distance + edge[2])
            if adj2[edge[1]].distance < dist_now:
                heapq.heappush(q2, (adj2[edge[1]].distance, adj2[edge[1]]))

while len(q3) > 0:
    curr = heapq.heappop(q3)
    if curr[0] >= curr[1].distance:
        for edge in curr[1].edges:
            dist_now = adj3[edge[1]].distance
            adj3[edge[1]].distance = min(adj3[edge[1]].distance, curr[1].distance + edge[2])
            if adj3[edge[1]].distance < dist_now:
                heapq.heappush(q3, (adj3[edge[1]].distance, adj3[edge[1]]))


v12 = adj1[v1].distance + adj2[v2].distance + adj3[V].distance
v21 = adj1[v2].distance + adj3[v1].distance + adj2[V].distance
result = min(v12, v21)
if math.isinf(result):
    print("-1")
else:
    print(result)