N, S = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

min_length = N*2

i, j = 0, 1
part_sum = numbers[0]


while i < N and j <= N:

    if j == N and part_sum < S:
        break

    if part_sum < S and j < N:
        part_sum += numbers[j]
        j += 1
    else:
        part_sum -= numbers[i]
        i += 1

    if i < j and  part_sum >= S and j-i < min_length:
        min_length = j-i


print(0 if min_length == N*2 else min_length)