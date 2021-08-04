import sys

n, m = [int(x) for x in input().split()]

database = {}
result = []
for i in range(n):
    cmd = sys.stdin.readline().strip().split()
    database[cmd[0]] = cmd[1]
for j in range(m):
    cmd = sys.stdin.readline().strip()
    result.append(database[cmd])
print("\n".join(result))

