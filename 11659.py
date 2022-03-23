
# 입력 파싱
N, M = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
ranges = []
for _ in range(M):
    i, j = [int(x) for x in input().split()]
    ranges.append((i, j))

# 누적합 O(n) 계산
culm_sum = [0] * N
culm_sum[0] = numbers[0]
for i in range(1, N):
    culm_sum[i] = culm_sum[i-1] + numbers[i]

culm_sum.insert(0, 0)

# 구간에 대해 한 번의 뺄셈으로 구간합 계산
for r in ranges:
    i, j = r[0], r[1]

    rangesum = culm_sum[j] - culm_sum[i-1]
    print(rangesum)

