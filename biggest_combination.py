import functools


nums = [3, 30, 34, 5, 9]

comparator = lambda a, b: str(a) + str(b) < str(b) + str(a)

def largest_number(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and comparator(nums[j-1], nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
            
    print(str(int("".join(map(str, nums)))))

largest_number(nums)

print(str(int("".join(
    map(str, sorted(nums, key=functools.cmp_to_key(comparator)))
    ))))