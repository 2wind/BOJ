class Node():
    def __init__(self, item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)



def convert_tree(tree_list, n):
    head = Node(tree_list[n])

    if 2*n+1 >= len(tree_list):
        return head

    if tree_list[2*n+1]:
        head.left = convert_tree(tree_list, 2*n+1)

    if tree_list[2*n+2]:
        head.right = convert_tree(tree_list, 2*n+2)

    return head


def get_tree(head):
    if head:
        print(head)
        get_tree(head.left)
        get_tree(head.right)


if __name__ == "__main__":
    binary_tree_list = [3, 9, 20, None, None, 15, 7]
    root = convert_tree(binary_tree_list, 0)
    get_tree(root)
