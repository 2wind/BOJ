

# method 1: create Node and print postorder


from collections import deque


class Node:
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None

def create_tree(preorder, in_i, in_j):
    if in_i < in_j:
        index = inorder.index(preorder.popleft(), in_i, in_j)

        node = Node(inorder[index])
        node.left = create_tree(preorder,in_i, index)
        node.right = create_tree(preorder,index+1, in_j)

        return node

def print_post(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)
            result.append(str(node.item))



    return result[::-1]

# number of test cases
T = int(input())

for _ in range(T):
    n = int(input()) # node count
    preorder = deque([int(x) for x in input().split()])
    inorder = [int(x) for x in input().split()]
    
    root = create_tree(preorder, 0, n)

    postorder = print_post(root)
    print(" ".join(postorder))


