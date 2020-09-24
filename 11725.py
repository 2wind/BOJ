import copy
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def put(self, node):
        if self.left == None:
            self.left = node
        elif self.right == None:
            self.right = node
        else:
            pass

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

link2 = copy.deepcopy(link)

# list connected
tree = []

node = Node(number)
def link_to_tree(node, link2):
    for i in link2[number]:
        n_i = Node(i)
        n_i = link_to_tree(n_i)
        node.put(n_i)

    link2 = [n.remove(x) for x in link2[number] for n in link2]

    return node




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