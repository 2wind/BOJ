from collections import deque

N, M, V = [int(x) for x in input().split()]

# 인접 그래프, 각 노드는 이동 가능한 노드들과 방문 여부를 나타냄
graph = [[False, []] for _ in range(N+1)]

for _ in range(M):
    p, q = [int(x) for x in input().split()]
    # 양방향
    graph[p][1].append(q)
    graph[q][1].append(p)

# 인접 리스트 정렬
for n in graph:
    n[1].sort()

DQ = deque()
dfs_result = []
bfs_result = []

# DFS
DQ.append(V)

while DQ:
    current = DQ.pop()
    # 종료 조건 설정
    if graph[current][0]:
        continue
    
    # 방문 처리
    graph[current][0] = True
    dfs_result.append(str(current))

    # 주위 순회
    for i in range(len(graph[current][1])-1, -1, -1):
        DQ.append(graph[current][1][i])


# 방문 리셋
for n in graph:
    n[0] = False

# BFS
DQ.append(V)

while DQ:
    current = DQ.popleft()
    # 종료 조건 설정
    if graph[current][0]:
        continue
    
    # 방문 처리
    graph[current][0] = True
    bfs_result.append(str(current))

    # 주위 순회
    for n in graph[current][1]:
        DQ.append(n)

print(" ".join(dfs_result))
print(" ".join(bfs_result))
