import sys
import math
from collections import deque
import heapq


class Node():
    def __init__(self, number):
        self.number = number
        self.distance = 2200000000

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


TC = int(input())
for i in range(TC):
    N, M, W = [int(x) for x in sys.stdin.readline().strip().split()] # Node number, Road number, Wormhole number
    adj = [Node(x) for x in range(N+1)]
    edges = deque()
    for j in range(M):
        S, E, T = [int(x) for x in sys.stdin.readline().strip().split()] # S -- T --> E
        edges.append((S, E, T))
        edges.append((E, S, T))
    for k in range(W):
        S, E, T = [int(x) for x in sys.stdin.readline().strip().split()] # S -- T --> E
        edges.append((S, E, -T))

    adj[1].distance = 0

    for i in range(1,N+1):
        for edge in edges:
            if adj[edge[0]].distance + edge[2] < adj[edge[1]].distance:
                adj[edge[1]].distance = adj[edge[0]].distance + edge[2]
    
    negative_cycle = False

    for edge in edges:
        if adj[edge[0]].distance + edge[2] < adj[edge[1]].distance:
            negative_cycle = True
            break

    print("YES") if negative_cycle else print("NO")


