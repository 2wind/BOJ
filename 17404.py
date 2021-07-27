import sys

N = int(input())

houses = [[0, 0, 0] for i in range(N)]
pricesR = [[0, 0, 0] for i in range(N)]
pricesG = [[0, 0, 0] for i in range(N)]
pricesB = [[0, 0, 0] for i in range(N)]


def update_price(prices, houses, i):
    prices[i][0] = min(prices[i-1][2], prices[i-1][1]) + houses[i][0]
    prices[i][1] = min(prices[i-1][0], prices[i-1][2]) + houses[i][1]
    prices[i][2] = min(prices[i-1][1], prices[i-1][0]) + houses[i][2]

for i in range(N):
    houses[i] = [int(x) for x in sys.stdin.readline().strip().split()]
    if i == 0:
        pricesR[i] = [houses[i][0], sys.maxsize, sys.maxsize]
        pricesG[i] = [sys.maxsize, houses[i][1], sys.maxsize]
        pricesB[i] = [sys.maxsize, sys.maxsize, houses[i][2]]
    elif i == N-1:
        pricesR[i] = [sys.maxsize, min(pricesR[i-1][0], pricesR[i-1][2]) + houses[i][1], min(pricesR[i-1][1], pricesR[i-1][0]) + houses[i][2]]
        pricesG[i] = [min(pricesG[i-1][2], pricesG[i-1][1]) + houses[i][0], sys.maxsize, min(pricesG[i-1][1], pricesG[i-1][0]) + houses[i][2]]
        pricesB[i] = [min(pricesB[i-1][2], pricesB[i-1][1]) + houses[i][0], min(pricesB[i-1][0], pricesB[i-1][2]) + houses[i][1], sys.maxsize]
    else:
        update_price(pricesR, houses, i)
        update_price(pricesG, houses, i)
        update_price(pricesB, houses, i)

print(min(min(pricesR[N-1]), min(pricesG[N-1]), min(pricesB[N-1])))