import sys
from collections import deque

class Node:
    def __init__(self, item = None, left = None, right = None, height = 1):
        self.item = item
        self.left = left
        self.right = right
        self.height = height

    def __str__(self):
        return str(self.item) + " "+ str(self.height)


def insert(node, item):
    if item < node.item:
        if node.left:
            insert(node.left, item)
        else:
            node.left = Node(item, None, None, node.height + 1)
    else:
        if node.right:
            insert(node.right, item)
        else:
            node.right = Node(item, None, None, node.height + 1)

def get_tree(head):
    if head:
        print(head)
        get_tree(head.left)
        get_tree(head.right)

def get_height(head):
    if head:
        print(head.height)
        return head.height + get_height(head.left) + get_height(head.right)
    else:
        return 0


N = int(input())
for i in range(N):
    item = int(sys.stdin.readline().strip())
    if i == 0:
        root = Node(item)
    else:
        insert(root, item)


# get_tree(root)
print(get_height(root))