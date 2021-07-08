from collections import deque
import sys

T = int(input())
for i in range(T):
    n = int(input())
    first = [int(x) for x in sys.stdin.readline().strip().split()]
    second = [int(x) for x in sys.stdin.readline().strip().split()]
    sol = [[0 for j in range(n)] for i in range(3)]
    sol[0][0] = first[0]
    sol[1][0] = second[0]
    for i in range(1,n):
        sol[0][i] = max(sol[1][i-1], sol[2][i-1]) + first[i]
        sol[1][i] = max(sol[0][i-1], sol[2][i-1]) + second[i]
        sol[2][i] = max(sol[0][i-1], sol[1][i-1])

    # print(sol[0])
    # print(sol[1])
    # print(sol[2])
    print(max(sol[0][n-1], sol[1][n-1], sol[2][n-1]))