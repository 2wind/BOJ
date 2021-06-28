import sys
sys.setrecursionlimit(10**9)
class Node:

    def __init__(self, element):
        self.element = element
        self.children = []
        self.parent = None
        self.visited = False

    def __str__(self):
        return str(self.element)

    def link(self, node):
        self.children.append(node)

    
def traverse_and_mark(n, parent):

    if n is not None and not n.visited:
            n.visited = True
            n.parent = parent
            for child in n.children:
                traverse_and_mark(child, n)
    

N = int(input())
nodes = []
for i in range(N+1):
    nodes.append(Node(i))


for i in range(N-1):
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    
    nodes[a].link(nodes[b])
    nodes[b].link(nodes[a])


traverse_and_mark(nodes[1], None)
parents = []
for i in range(2,len(nodes)):
    parents.append(str(nodes[i].parent))

print("\n".join(parents))
