

class Node:
    def __init__(self, item = None):
        self.item = item
        self.children = [None for _ in range(10)]
        self.end = False

    def __str__(self):
        return str(self.item)

# 만약 삽입시 leaf node에 삽입된다면 일관성이 없다.

def check_number(phone_number):
    node = root
    for digit in phone_number:
        if node.end:
            return False
        node = node.children[digit]
    return True

t = int(input())
for _ in range(t):
    root = Node()
    n = int(input())
    is_sound = True
    phone_book = []

    for i in range(n):
        phone_number = [int(x) for x in list(input())]
        phone_book.append(phone_number)
        node = root

        for digit in phone_number:
            if not node.children[digit]:
                node.children[digit] = Node(digit)
            node = node.children[digit]
        node.end = True

    for phone_number in phone_book:
        is_sound *= check_number(phone_number)


    print("YES") if is_sound else print("NO")