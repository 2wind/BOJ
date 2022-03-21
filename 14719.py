H, W = [int(x) for x in input().split()]
blocks = [int(x) for x in input().split()]

assert W == len(blocks)

volume = 0

left, right = 0, W - 1
left_max, right_max = blocks[left], blocks[right]

while left < right:
    left_max, right_max = max(left_max, blocks[left]), max(right_max, blocks[right])

    if left_max < right_max:
        volume += left_max - blocks[left]
        left += 1
    else:
        volume += right_max - blocks[right]
        right -= 1

print(volume)
