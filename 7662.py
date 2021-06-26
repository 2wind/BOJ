import bisect
import heapq
import sys

input = sys.stdin.readline

class delQ:
    
    def __init__(self):
        self.queue = []
        self.delqueue = []

    def insert(self, n):
        heapq.heappush(self.queue, n)

    def delete(self, n):
        heapq.heappush(self.delqueue, n)

    def adjust(self):

        while(len(self.delqueue) > 0 and self.queue[0] == self.delqueue[0]):
            heapq.heappop(self.queue)
            heapq.heappop(self.delqueue)

    def top(self):
        self.adjust()
        return self.queue[0]

    def __len__(self):
        return len(self.queue) - len(self.delqueue)

    def clear(self):
        self.queue.clear()
        self.delqueue.clear()



maxQ = delQ()
minQ = delQ()

def insert(n):
    
    maxQ.insert((-n, n))
    minQ.insert(n)

def remove_max():
    if len(maxQ) > 0:
        _, n = maxQ.top()
        maxQ.delete((-n, n))
        minQ.delete(n)


def remove_min():
    if len(minQ) > 0:
        n = minQ.top()
        maxQ.delete((-n, n))
        minQ.delete(n)

T = int(input().strip())
for i in range(T):
    maxQ.clear()
    minQ.clear()
    
    k = int(input().strip())
    for j in range(k):
        cmd = input().strip().split(" ")
        letter, num = cmd[0], int(cmd[1])

        if letter == "I":
            # insert(num, 0, len(dpque))
            insert(num)
            # bisect.insort(dpque, num, 0, len(dpque))
        elif num == 1:
            remove_max()
        else:
            remove_min()
        # print(dpque)

    if len(maxQ) <= 0:
        print("EMPTY")
    else:
        print(f"{maxQ.top()[1]} {minQ.top()}")
