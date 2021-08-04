import sys
from collections import deque
sys.setrecursionlimit(10**9)

class Node():
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.children = deque()
        self.weight = 0
        self.visited = False
    
    def __str__(self):
        return f"{str(self.parent)} \ {self.number}: {self.weight} - [{self.children}]"


n = int(input())

nodes = [Node(x) for x in range(n+1)]

for i in range(n-1):
    p, c, w = [int(x) for x in sys.stdin.readline().strip().split()]
    edge = (p, c, w)
    nodes[c].weight = nodes[p].weight + w
    nodes[c].parent = (nodes[p], w)
    nodes[p].children.append((nodes[c], w))


max_depth = max(nodes, key=lambda node: node.weight)
# print(max_depth)

def find_max_distance(node: Node, weight: int) -> int:
    # print(node)
    if not node.visited:
        node.visited = True
        distance = weight
        if node.parent:
            curr = find_max_distance(node.parent[0], node.parent[1])
            if distance < weight + curr:
                distance = weight + curr
        for child in node.children:
            curr = find_max_distance(child[0], child[1])
            if distance < weight + curr:
                distance = weight + curr
        # print(distance)
        return distance
    else:
        return 0

print(find_max_distance(max_depth, 0))

