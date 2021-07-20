import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))


count = 0
for i in range(N):
    perm = combinations(numbers, i+1)

    for p in perm:
        print(p)
        if sum(p) == S:
            count += 1


print(count)