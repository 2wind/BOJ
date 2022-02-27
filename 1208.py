from itertools import combinations
import sys
import bisect

# https://degurii.tistory.com/191

N, S = map(int, sys.stdin.readline().strip().split())
numbers = [int(x) for x in sys.stdin.readline().strip().split()]

upper, lower = numbers[:N//2], numbers[N//2:]

com_upper, com_lower = [], []


for i in range(len(upper)+1):
    for com in combinations(upper, i):
        com_upper.append(sum(com))


for i in range(len(lower)+1):
    for com in combinations(lower, i):
        com_lower.append(sum(com))



answer = 0

com_lower.sort()
# print(com_upper, com_lower)

for a in com_upper:

    upper = bisect.bisect_right(com_lower, S - a)
    lower = bisect.bisect_left(com_lower, S - a)
    # print(S-a)
    # print(lower, upper)
    # print(sum(1 for x in com_lower if x == S - a))
    # assert(upper - lower == sum(1 for x in com_lower if x == S - a))

    answer += (upper - lower)


if S == 0:
    answer -= 1

print(answer)


