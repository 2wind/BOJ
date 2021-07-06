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

def divide_tree(inl, postl, in0, in1, post0, post1):
    # print(" " +" "*in0*5 + "i0")
    # print(" " +" "*in1*5 + "i1")
    # print(inl)
    # print(" " +" "*post0*5 + "p0")
    # print(" " +" "*post1*5 + "p1")
    # print(postl)

    if post0+1 == post1:
        # print(post1-1)
        node = Node(postl[post1-1])
        return node
    elif post0 < post1:
        # print(post1-1)
        root = postl[post1-1]
        i = inl.index(root, in0, in1+1)
        # print(f"i = {i}, root = {root}")
        node = Node(root)
        # print(f"{inl[in0:i]} | {root} | {inl[i+1:in1]}")
        # print(f"{postl[post0:post0+i-in0]} | {postl[post0+i-in0:post0+i-in0+(in1-(i+1))]} | {root}")
        node.left =divide_tree(inl, postl, in0, i   ,post0          ,  post0 + i-in0 )
        node.right=divide_tree(inl, postl, i+1, in1 , post0+i-in0   ,  post0+i-in0+(in1-(i+1)) )
        return node
    else:
        return None
    
    

root = divide_tree(inorder, postorder, 0, len(inorder), 0, len(postorder))

def preorder(node, q):
    
    q.append(str(node))
    if node.left:
        preorder(node.left, q)
    if node.right:
        preorder(node.right, q)

result = deque()
preorder(root, result)
print(" ".join(result))
