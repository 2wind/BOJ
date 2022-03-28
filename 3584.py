class Node:
    def __init__(self, item = None, parent = None):
        self.item = item
        self.parent = parent
        self.children = []


T = int(input())
for _ in range(T):
    n_to_node = dict()
    N = int(input())

    for _ in range(N-1):
        A, B = [int(x) for x in input().split()]

        if A in n_to_node:
            nodeA = n_to_node[A]
        else:
            nodeA =  Node(A)
            n_to_node[A] = nodeA
        if B in n_to_node:
            nodeB = n_to_node[B]
        else:
            nodeB = Node(B)
            n_to_node[B] = nodeB

        nodeA.children.append(nodeB)
        nodeB.parent = nodeA

    node1, node2 = [n_to_node[int(x)] for x in input().split()]
    first_parents = []

    while node1 is not None:
        first_parents.append(node1.item)
        node1 = node1.parent

    while node2 is not None:
        if node2.item in first_parents:
            print(node2.item)
            break
        node2 = node2.parent
