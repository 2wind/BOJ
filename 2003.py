N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

i, j = 0, 1
count = 0

while j <= N:
    s = sum(A[i:j])

    if s == M:
        count += 1
        i += 1
        j += 1

    elif s > M:
        i += 1
    
    else:
        j += 1

print(count)