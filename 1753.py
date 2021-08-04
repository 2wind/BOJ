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
K = int(input()) # Starting node K

adj = [Node(x) for x in range(V+1)]

for i in range(E):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    adj[a].edges.append((a, b, c))

adj[K].visited = True
adj[K].distance = 0

q = []

for node in adj[1:]:
    heapq.heappush(q, (node.distance, node))

while len(q) > 0:
    curr = heapq.heappop(q)
    if curr[0] >= curr[1].distance:
        for edge in curr[1].edges:
            dist_now = adj[edge[1]].distance
            adj[edge[1]].distance = min(adj[edge[1]].distance, curr[1].distance + edge[2])
            if adj[edge[1]].distance < dist_now:
                heapq.heappush(q, (adj[edge[1]].distance, adj[edge[1]]))
        
for i in range(1, V+1):
    print(adj[i])