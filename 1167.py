import sys
from collections import deque
sys.setrecursionlimit(10**9)

class Node():
    def __init__(self, number):
        self.number = number
        self.linked = deque()
        self.weight = 0
        self.visited = False
    
    def __str__(self):
        return f"{self.number}: {self.weight} - [{self.linked}]"


V = int(input())

nodes = [Node(x) for x in range(V+1)]

for i in range(V):
    line = [int(x) for x in sys.stdin.readline().strip().split()]
    p = line[0]
    index = 1
    while line[index] != -1:
        c, w = line[index], line[index+1]
        nodes[p].linked.append((nodes[c], w))
        index += 2

stack = deque()
stack.append((nodes[1], 0, 0))
while len(stack) > 0:
    top, w, prev = stack.pop()
    if not top.visited:
        top.visited = True
        top.weight = prev + w
        for child in top.linked:
            stack.append((child[0], child[1], top.weight))


# print(nodes)

max_depth = max(nodes, key=lambda node: node.weight)
# print(max_depth)


def find_max_distance(node: Node, weight: int) -> int:
    # print(node)
    if node.visited:
        node.visited = False
        distance = weight
        for child in node.linked:
            curr = find_max_distance(child[0], child[1])
            if distance < weight + curr:
                distance = weight + curr
        # print(distance)
        return distance
    else:
        return 0

print(find_max_distance(max_depth, 0))
