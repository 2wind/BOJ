import sys
import bisect


N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

# LIS = [[A[0]]]
LIS_last = [sys.maxsize for i in range(N)]
LIS_last[0] = A[0]
LIS_length = 1
track = []

for i in range(N):
    # print("LIS:", LIS[-1], "A[i]=", A[i])
    
    if LIS_last[LIS_length-1] < A[i]:
        LIS_length += 1
        LIS_last[LIS_length-1] = A[i]
        track.append((A[i], LIS_length-1))
    else:
        idx = bisect.bisect_left(LIS_last, A[i])
        LIS_last[idx] = A[i] # insert at lower bound
        track.append((A[i], idx))
    # print(LIS_last)
    # print(LIS)
    # print(LIS_last, LIS_length)


index = LIS_length -1
for i in range(len(track)-1, -1, -1):
    pair = track[i]
    if pair[1] == index:
        LIS_last[index] = pair[0]
        index -= 1

print(LIS_length)
print(" ".join(map(str, LIS_last[:LIS_length])))