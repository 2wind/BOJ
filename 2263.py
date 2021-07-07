import sys
from collections import deque
n = int(input())
inorder = input().split()
postorder = input().split()

# print(inorder)
# print(postorder)


class Node():
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.num)

def divide_tree(inl, postl, in0, in1, post0, post1, parents):
    # print(" " +" "*in0*5 + "i0")
    # print(" " +" "*in1*5 + "i1")
    # print(inl)
    # print(" " +" "*post0*5 + "p0")
    # print(" " +" "*post1*5 + "p1")
    # print(postl)

    stack = deque()
    stack.append((in0, in1, post0, post1, False))

    
    while len(stack) > 0:
        in0, in1, post0, post1, is_left = stack.pop()

        if post0 < post1:
            # print(post1-1)
            root = postl[post1-1]
            i = inl.index(root, in0, in1+1)
            # print(f"i = {i}, root = {root}")
            node = Node(root)
            # print(f"{inl[in0:i]} | {root} | {inl[i+1:in1]}")
            # print(f"{postl[post0:post0+i-in0]} | {postl[post0+i-in0:post0+i-in0+(in1-(i+1))]} | {root}")
            if len(parents) > 0:
                if is_left:
                    parents[-1].left = node
                else:
                    parents[-1].right = node
            stack.append((i+1, in1 , post0+i-in0   ,  post0-in0+in1-1, False))
            stack.append((in0, i   ,post0          ,  post0 + i-in0 , True))
            
            parents.append(node)

    
parents = deque()
divide_tree(inorder, postorder, 0, len(inorder), 0, len(postorder), parents)

# def preorder(node, q):
    
#     q.append(str(node))
#     if node.left:
#         preorder(node.left, q)
#     if node.right:
#         preorder(node.right, q)

# for i in parents:
#     print(i)
# result = deque()
# preorder(parents[0], result)
print(" ".join([str(x) for x in parents]))
