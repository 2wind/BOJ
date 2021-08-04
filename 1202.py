import heapq
import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
gems = []
heap = []
bags = []

for i in range(N):
    M, V = [int(x) for x in sys.stdin.readline().split()]
    gems.append((M, V))
    # heapq.heappush(gems, (-V/M, M, V))

for i in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)
    
gems.sort(key=lambda x: x[0])
bags.sort()

# print(gems)

# print(bags)
price = 0
i = 0
for bag in bags:
    while i < N and bag >= gems[i][0]:
        heapq.heappush(heap, -gems[i][1])
        i += 1
    if heap:
        price -= heapq.heappop(heap)

print(price)

