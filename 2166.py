import sys

N = int(input())
m = [[0, 0] for i in range(N+1)]
for i in range(N):
    m[i] = [int(x) for x in sys.stdin.readline().strip().split()]

m[-1] = m[0]
# print(m)

sum1 = 0
for i in range(N):
    sum1 += m[i][0] * m[i+1][1]
# print(sum1)

sum2 = 0
for i in range(N):
    sum2 += m[i+1][0] * m[i][1]
# print(sum2)

sol = 0.5 * abs(sum1 - sum2)
print(f"{round(sol, 1)}")