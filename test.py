import sys
from collections import deque
n = int(input())
inorder = input().split()
postorder = input().split()
sys.setrecursionlimit(10**9)
# print(inorder)
# print(postorder)

class Node():
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.num)

def divide_tree(inl, postl):
    print(inl, postl)
    if len(postl) > 0:
        root = postl[-1]
        print(root)
        i = inl.index(root)
        node = Node(root)
        node.right = divide_tree(inl[i+1:], postl[i:-1])
        node.left = divide_tree(inl[:i], postl[:i])
        return node
    else:
        return None
    
    

root = divide_tree(inorder, postorder)

def preorder(node):
    
    result = [str(node)]
    if node.left:
        result += preorder(node.left)
    if node.right:
        result += preorder(node.right)
    return result

print(" ".join(preorder(root)))
