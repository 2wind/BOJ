import sys

class Node:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.element)

    
class Tree:

    def __init__(self):
        self.root = None
    
    def find_r(self, letter, node):
        
        if node is None:
            return None
        elif node.element == letter:
            return node
        else:
            return self.find_r(letter, node.left) or self.find_r(letter, node.right)


    def find(self, letter):
        return self.find_r(letter, self.root)

        
    def insert(self, curr, left, right):
        node = self.find(curr)
        if node is None:
            self.root = Node(curr)
            if left != ".":
                self.root.left = Node(left)
            if right != ".":
                self.root.right = Node(right)
        else:
            if left != ".":
                node.left = Node(left)
            if right != ".":
                node.right = Node(right)

    def preorder(self, node):
        if node is None:
            return
        else:
            sys.stdout.write(str(node))
            self.preorder(node.left)
            self.preorder(node.right)


    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            sys.stdout.write(str(node))
            self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            sys.stdout.write(str(node))



T = int(input())
tree = Tree()

for i in range(T):
    curr, left, right = input().split()
    tree.insert(curr, left, right)

tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)
print("")