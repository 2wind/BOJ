import sys
import bisect


N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

LIS = [[A[0]]]
LIS_last = [A[0]]

for i in range(1, N):
    # print("LIS:", LIS[-1], "A[i]=", A[i])
    
    if LIS[-1][-1] < A[i]:
        # print("Append")
        LIS.append(LIS[-1] + [A[i]])
        LIS_last.append(A[i])
    else:
        # print("Change")
        idx = bisect.bisect_left(LIS_last, A[i])
        # print("idx:",idx)
        LIS_last[idx] = A[i] # insert at lower bound
        replaced = LIS[idx-1] if idx > 0 else []
        LIS[idx] = replaced + [A[i]] # insert at lower bound
    # print(LIS_last)
    # print(LIS)

print(len(LIS[-1]))
print(" ".join(map(str, LIS[-1])))