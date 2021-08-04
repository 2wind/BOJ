from collections import deque
import sys

class Node():
    def __init__(self, index, linkedto):
        self.index = index
        self.linkedto = linkedto
        self.visited = False
        self.stack_index = -1
        

T = int(input())

for i in range(T):
    n = int(input())
    
    students = deque()
    students.appendleft(None)
    students += [Node(idx +1, int(x)) for idx, x in enumerate(sys.stdin.readline().strip().split())]

    
    one_team = 0
    stack = deque()
    visiteds = set()
    for j in range(1, n+1):
        current = students[j]
        if current.visited:
            continue
        stack.clear()
        visiteds.clear()
        stack.append(students[j])
        stack_index = 0
        while True:
            node = stack[-1]
            if not node.visited:
                node.visited = True
                node.stack_index = stack_index
                visiteds.add(node.index)
                linked_node = students[node.linkedto]
                if linked_node.index in visiteds:
                    one_team += (stack_index - linked_node.stack_index + 1)
                    break
                else:
                    stack.append(linked_node)
                    stack_index += 1
            else:
                break


    print(n - one_team)
        



