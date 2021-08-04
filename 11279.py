import heapq
import sys

heap = []

def push(number):
    heapq.heappush(heap, -1 * number)

def pop():
    if not heap:
        return 0
    return -1 * heapq.heappop(heap)

N = int(input())
for i in range(N):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        print(pop())
    else:
        push(cmd)