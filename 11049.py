import sys

N = int(input())
m = [(0, 0) for j in range(N+1)]

dp = [[0 for j in range(N+2)] for i in range(N+2)]
for i in range(N):
    P, Q = [int(x) for x in sys.stdin.readline().strip().split()]
    m[i+1] = (P, Q)

# print(m)
# for i in range(N-1):
#     matrices[1][i] = dot(matrices[0][i], matrices[0][i+1])

for i in range(1, N):
    for j in range(1, N-i+1):
        dp[j][i+j] = sys.maxsize
        for k in range(j, i+j+1):
            dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + m[j][0] * m[k][1] * m[i+j][1])

# print(dp)

print(dp[1][N])