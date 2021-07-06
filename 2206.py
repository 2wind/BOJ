import sys
from collections import deque

N, M = [int(x) for x in input().split()]

roadmap = deque()

for i in range(N):
    line = sys.stdin.readline().strip()

    roadmap.append(deque(list(line)))

# print(roadmap)
visited = [[[False, False] for y in range(M)] for x in range(N)]
# print(visited)


queue = deque()

queue.append((0, 0, False, 1))

def get_valid(i, j):
    valid = []
    if i > 0:
        valid.append((i-1, j))
    if i < N-1:
        valid.append((i+1, j))
    if j > 0:
        valid.append((i, j-1))
    if j < M-1:
        valid.append((i, j+1))
    return valid

dest_distance = -1
while len(queue) > 0:
    i, j, wall_broken, distance = queue.pop()
    # print(i, j, wall_broken, distance)
    if i == N-1 and j == M-1:
        dest_distance = distance
        break
    if not wall_broken:
        if not visited[i][j][0]:
            # print(visited[i][j][0])
            visited[i][j][0] = True
            candidates = get_valid(i, j)
            for coord in candidates:
                p, q = coord
                if roadmap[p][q] == "1":
                    queue.appendleft((p, q, True, distance + 1))
                else:
                    queue.appendleft((p, q, False, distance + 1))
    else:
        if not visited[i][j][1]:
            visited[i][j][1] = True
            candidates = get_valid(i, j)
            for coord in candidates:
                p, q = coord
                if roadmap[p][q] == "0":
                    queue.appendleft((p, q, True, distance + 1))

print(dest_distance)