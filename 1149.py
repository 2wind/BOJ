import sys

N = int(input())

houses = [[0, 0, 0] for i in range(N)]
prices = [[0, 0, 0] for i in range(N)]

for i in range(N):
    houses[i] = [int(x) for x in sys.stdin.readline().strip().split()]
    if i == 0:
        prices[i] = houses[i]
    else:
        prices[i][0] = min(prices[i-1][2], prices[i-1][1]) + houses[i][0]
        prices[i][1] = min(prices[i-1][0], prices[i-1][2]) + houses[i][1]
        prices[i][2] = min(prices[i-1][1], prices[i-1][0]) + houses[i][2]

print(min(prices[N-1]))