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


n, m = map(int, sys.stdin.readline().strip().split())

dots = DSet(list(range(n)))


sol = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if sol > 0:
        continue
    elif sol == 0 and dots.find(a) == dots.find(b):
        sol = i+1
    else:
        dots.union(a, b)
print(sol)



