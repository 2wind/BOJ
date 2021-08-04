import sys

n, m = [int(x) for x in input().split()]
deut, bo = set(), set()
for i in range(n):
    deut.add(sys.stdin.readline())
for j in range(m):
    bo.add(sys.stdin.readline())
    
result = sorted(list(deut & bo))
print(len(result))
print("".join(result).strip())
