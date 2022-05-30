import sys
N, H = [int(x) for x in input().split()]
obstacles = [0 for _ in range(H)]

for i in range(N):
    h = int(sys.stdin.readline().strip())
    obstacles[h] += 1
    

for o in obstacles:
    

minimum = min(obstacles)
counts = obstacles.count(minimum)
print(minimum, counts)
            