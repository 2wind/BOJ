N = int(input())

nums = [int(x) for x in input().split(' ')]
assert N == len(nums)

target = int(input())

nums_map = {}
answers = 0

for i, n in enumerate(nums):
    nums_map[n] = i

for i, n in enumerate(nums):
    complement = target - n
    if complement in nums_map and i < nums_map[complement]:
        answers += 1

print(answers)
