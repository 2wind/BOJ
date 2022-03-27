import sys
import math

def calc_dist(node_from, node_to):
    height_from, height_to = mountains[node_from], mountains[node_to]
    if abs(height_from - height_to) > T:
        return math.inf
    if height_from >= height_to:
        return 1
    else:
        return (height_to - height_from) ** 2

# dict from alpahbet to height
a2h = dict()
for i in range(ord("A"), ord("Z")+1):
    a2h[chr(i)] = i - ord("A")

for i in range(ord("a"), ord("z")+1):
    a2h[chr(i)] = i - ord("a") + 26

N, M, T, D = map(int, input().split())
mountains = []
for _ in range(N):
    mountains.extend([a2h[x] for x in list(sys.stdin.readline().rstrip())])

# 노드 초기화, 노드를 풀어헤쳐 리스트로 단순화함 (0..M*N-1)
nodes = [i * M + j for j in range(M) for i in range(N)]
# 거리 초기화, 노드를 풀어헤쳐 2중 리스트로 단순화함
# let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
dists = [[math.inf for _ in range(N * M)] for _ in range(N * M)]
# 변의 가중치와 자기 자신으로 가는 가중치 업데이트
for node in nodes: # O(n)
    dists[node][node] = 0
    for node_to in [(node+1), (node-1), (node+M), (node-M)]:
        if abs(node - node_to) == 1 and node // M != node_to // M:
            continue
        if node_to < 0 or node_to >= N*M:
            continue
        dists[node][node_to] = calc_dist(node, node_to)

# 플로이드-와샬 (k, i, j 삼중 for문 이용)
for k in nodes: # O(n^3)
    for i in nodes:
        for j in nodes:
            # 만약 i --> j 보다 i --> k --> j가 더 짧다면 갱신!
            dists[i][j] = min(dists[i][k] + dists[k][j], dists[i][j])

# 최대로 갈 수 있는 높이 계산
max_height = -1
for node in nodes: # O(n)
    round_trip = dists[0][node] + dists[node][0]
    if round_trip <= D:
        max_height = max(max_height, mountains[node])

print(max_height)

