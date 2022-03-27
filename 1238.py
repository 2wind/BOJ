from collections import defaultdict
import heapq
N, M, X = [int(x) for x in input().split()]

graph = defaultdict(list)
dists = defaultdict(int)

for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    graph[u].append((v, w)) # u --> [(v1, w1), ...]

# 1, 2, .. --> X --> 1, 2, ..

for i in range(1, N+1):
    PQ = [(0, i)] # distance, node
    dist = defaultdict(int)

    while PQ:
        d, node = heapq.heappop(PQ)
        if node not in dist:
            dist[node] = d

            for v, w in graph[node]:
                alt = d + w
                heapq.heappush(PQ,(alt, v))
    dists[i] += dist[X]
    if (i == X):
        for j in range(1, N+1):
            dists[j] += dist[j]
    
print(max(dists.values()))
