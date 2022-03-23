import heapq

heap = []
N = int(input())

result = []
for _ in range(N):
    x = int(input())
    if x == 0:
        output = 0
        if heap:
            output = heapq.heappop(heap)[1]
        result.append(str(output))

    else:
        heapq.heappush(heap, (abs(x), x))


print("\n".join(result))
