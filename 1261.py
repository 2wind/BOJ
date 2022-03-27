from collections import defaultdict
import heapq

M, N = [int(x) for x in input().split()]
maze = []
for i in range(N):
    row = [int(x) for x in list(input())]
    maze.append(row)

# print(maze)

Q = [(0, (0, 0))] # (소요 시간, 정점) 으로 구성된 우선순위 큐(heapq로 조작함)
dist = defaultdict(int) # 정점: 소요 시간으로 구성된 딕셔너리
visited = set()

while Q:
    time, node = heapq.heappop(Q)
    if node not in dist and node not in visited:
        # 만약 소요시간 갱신이 되어있지 않는다면 갱신해주고 푸시
        visited.add(node)
        dist[node] = time
        i, j = node
        # 이웃 노드에 대해
        for p, q in [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]:
            if p < 0 or q < 0 or p >= N or q >= M:
                continue
            cost = maze[p][q]
            # 비용 함수 계산
            alt = time + cost
            # 비용 갱신
            heapq.heappush(Q, (alt, (p, q)))

print(dist[(N-1, M-1)])
        