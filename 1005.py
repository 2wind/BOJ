import sys
from collections import deque
import heapq

class Node():
    def __init__(self, n):
        self.time = n
        self.timesum = -1
        self.linkfrom = []
        self.linkto = []
        self.fromcount = 0

    def __gt__(self, value):
        if self.fromcount == value.fromcount:
            return self.time > value.time

        else:
            return self.fromcount > value.fromcount
        

def find_timesum(node):
    if not node.linkfrom:
        return node.time
    else:
        return node.time + max(map(find_timesum, node.linkfrom))
        


T = int(input())
for i in range(T):
    N, K = [int(x) for x in input().split()]
    buildings = [Node(int(x)) for x in input().split()]
    buildings = [Node(-1)] + buildings

    for k in range(K):
        X, Y = [int(x) for x in input().split()]
        buildings[X].linkto.append(buildings[Y])
        buildings[Y].linkfrom.append(buildings[X])
        buildings[Y].fromcount += 1

    W = int(input())
    target = buildings[W]
    # recursive first
    # recursive = find_timesum(target)

    stack = deque()
    disQ = []
    resultQ = deque()

    tpsort = deque()

    for b in buildings:
        if b.fromcount == 0:
            heapq.heappush(disQ, (b.fromcount, b))

    while disQ:
        fromcount, node = heapq.heappop(disQ)
        tpsort.append(node)
        for child in node.linkto:
            child.fromcount -= 1
            if child.fromcount == 0:
                heapq.heappush(disQ, (child.fromcount, child))

    for building in tpsort:
        if building.timesum < 0:
            if len(building.linkfrom) == 0:
                building.timesum = building.time
            else:
                building.timesum = building.time + max(map(lambda x: x.timesum, building.linkfrom))
    # stack.append((target, None))
    # while stack:
    #     building, parent = stack.pop()
    #     tpsort.appendleft((building, parent))

    #     for b in building.linkfrom:
    #         stack.append((b, building))

    # for building, parent in tpsort:
    #     if parent is not None:
    #         if building.time + building.timesum > parent.timesum:
    #             parent.timesum = building.time + building.timesum

    iterative = target.timesum
    # assert(recursive == iterative)
    print(iterative)
        

    