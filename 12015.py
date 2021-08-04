import sys
import bisect


N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

LIS = [A[0]]

for i in range(1, N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i] # insert at lower bound
print(len(LIS))