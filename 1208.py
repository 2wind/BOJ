import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [[0 for j in range(N+1)] for i in range(N)]



for i in range(N):
    dp[i][i] = 1 # 0자리면 palindrome
    dp[i][i+1] = 1 # 1자리면 palindrome

for k in range(2, N+1):
    for i in range(0, N+1-k):
        j = i+k
        dp[i][j] = 1 if dp[i+1][j-1] == 1 and numbers[i] == numbers[j-1] else 0


M = int(sys.stdin.readline())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S-1][E])


