class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

N = int(input())
link = [False] * (N + 1)

def connect(a, b):
    if not link[a]:
        link[a] = [b]
    else:
        link[a].append(b)

for i in range(N-1):
    (first, second) = [int(x) for x in input().split()]
    connect(first, second)
    connect(second, first)

# list connected
tree = []
def add(number):
    new_node = Node(number)
    connected = link[number]
    if len(connected) > 0:
        # find any connected(=parent?) node from tree
        # connect root to parent

        if len(connected) == 1:
            pass
        elif len(connected) == 2:
            pass
        elif len(connected) == 3:
            pass
            # make connected node(s) and connect to node

# sort tree by node.data
# print parent from i = 2 .. n - 1

for i in link:
    print(i)