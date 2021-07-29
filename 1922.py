import heapq
import sys

class DSet():
    class Node:
        def __init__(self, key):
            self.parent = self
            self.rank = 0

    def __init__(self, keys):
        self.nodes = {}
        for key in keys:
            self.nodes[key] = self.Node(key)

    def create(self, key):
        if key not in self.nodes:
            self.nodes[key] = self.Node(key)


    def find(self, key):
        node = self.nodes[key]
        while node.parent != node:
            node, node.parent = node.parent, node.parent.parent
        return node

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            # Union by rank
            if x.rank < y.rank:
                x, y = y, x
            y.parent = x
            if x.rank == y.rank:
                x.rank += 1


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

edgeQ = []
dset = DSet(list(range(1, V+1)))
MST = 0
length = 0

for i in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    edge1 = (C, A, B)
    edge2 = (C, B, A)
    edgeQ.append(edge1)
    edgeQ.append(edge2)


heapq.heapify(edgeQ)

while length < V-1:
    smallest = heapq.heappop(edgeQ)
    if dset.find(smallest[1]) != dset.find(smallest[2]):
        MST += smallest[0]
        length += 1
        dset.union(smallest[1], smallest[2])


    
print(MST)