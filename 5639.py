

from collections import deque


class Node:
    def __init__(self, item = None) -> None:
        self.item = item
        self.left = None
        self.right = None
        

def insert(node, item):
    if node:
        if node.item > item:
            if not node.left:
                node.left = Node(item)
            else:
                insert(node.left, item)
        else:
            if not node.right:
                node.right = Node(item)
            else:
                insert(node.right, item)
                
def insert_iter(item):
    node = root
    while node:
        if node.item > item:
            if not node.left:
                node.left = Node(item)
                break
            else:
                node = node.left
        else:
            if not node.right:
                node.right = Node(item)
                break
            else:
                node = node.right


preorder = []

while True:
    try:
        num = int(input())
        preorder.append(num)
    except:
        break


# insertion
for index, item in enumerate(preorder):
    if index == 0:
        root = Node(item)
    else:
        insert(root, item)

# postorder printing
Q = [root]
results = deque()

while Q:
    node = Q.pop()
    if node:
        Q.append(node.left)
        Q.append(node.right)
        results.appendleft(str(node.item))

print("\n".join(results))


