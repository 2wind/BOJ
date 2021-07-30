import sys


class DSet():
    def __init__(self, vertices = []):
        self.vertices = vertices
        self.parent = {}
        for vertex in self.vertices:
            self.parent[vertex] = vertex

    def find(self, element):
        if self.parent[element] == element:
            return element
        else:
            result = self.find(self.parent[element])
            self.parent[element] = result
            return result

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())

dset = DSet(list(range(G+1)))

planes = []
for i in range(P):
    gi = int(sys.stdin.readline().strip())
    planes.append(gi)

count = 0
for plane in planes:
    k = dset.find(plane)
    if k == 0:
        break
    dset.union(k, k-1)
    count += 1

print(count)
