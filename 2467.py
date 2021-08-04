import sys

N = int(input())
numbers = [int(x) for x in input().split()]

i, j = 0, len(numbers)-1

gmin = sys.maxsize
imin, jmin = i, j
while i < j:
    curr = numbers[i] + numbers[j]

    if abs(curr) < abs(gmin):
        gmin = curr
        imin, jmin = i, j
    if curr < 0 :
        i += 1
    elif curr > 0 :
        j -= 1
    else:
        break

print(numbers[imin], numbers[jmin])
