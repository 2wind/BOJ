import heapq

n = int(input())
stars = []
for _ in range(n):
    x, y = [float(x) for x in input().split()]
    stars.append([x, y, []])

def dist(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5

# 별들에 대해 서로간의 거리를 모두 계산 O(N^2)
for i, star1 in enumerate(stars):
    for j, star2 in enumerate(stars):
        if i != j:
            star1[2].append((dist(star1, star2), i, j))

# print(stars)

# 프림 알고리즘
verts = {0}
edges = stars[0][2][:]
edges_length = 0.0
heapq.heapify(edges)

for _ in range(n-1):
    # 인접 정점 중 최소 간선을 선택한다
    # 이 때 방문하지 않은 정점으로 이어질 때까지 반복해서 뽑는다
    while edges:
        shortest = heapq.heappop(edges)
        if shortest[2] not in verts:
            break

    # 선택한 간선의 길이를 더한다
    edges_length += shortest[0]

    # 최소 간선에 연결된 vert를 선택한다
    vert = shortest[2]
    verts.add(vert)

    # 추가한 vertices에 인접한, 방문하지 않은 간선들을 모조리 간선에 넣는다
    # 이 때 방문하지 않은 점으로 이어지는 간선만 넣는다
    for e in stars[vert][2]:
        if e[2] not in verts:
            heapq.heappush(edges, e)

    # print(shortest, vert)

print(edges_length)