t = int(input())

for _ in range(t):
    n, K = [int(x) for x in input().split(' ')]
    nums = [int(x) for x in input().split(' ')]
    assert n == len(nums)
    
    nums.sort()

    left, right = 0, n-1

    smallest_diff = K # 적당한 숫자로 조정. 
    summations = 0

    while not left == right:
        summation = nums[left] + nums[right]
        diff = abs(K - summation)

        # 만약 차이가 더 작은 합을 찾으면
        if diff < smallest_diff:
            summations = 1
            smallest_diff = diff

        # 차이가 동일하면
        elif diff == smallest_diff:
            summations += 1

        # 그 뒤 갈 방향을 정한다.
        if summation < K :
            left += 1

        elif summation > K:
            right -= 1

        else:
            left += 1
            right -= 1

    print(summations)