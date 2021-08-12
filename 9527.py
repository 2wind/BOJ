import sys
import math

def any_sum(X, Y): # bin sum of [2 ** i, Y), X = 2 ** i
    i = int(math.log2(X))
    if X == Y: # 범위가 0인 경우
        return 0
    elif X == Y - X: # 정확히 한 칸 차이나는 경우
        return part_sum(i)
    elif X // 2 >= Y - X: # 
        return any_sum(X // 2,  Y - X // 2)
    elif X > Y-X:
        return part_sum(i-1) + (Y-X - X // 2) + any_sum(X, Y - X//2)
    elif math.log2(Y) % 1 == 0:
        return any_sum(X, Y // 2) + part_sum(Y // 2)
    else:
        j = math.floor(math.log2(Y))
        return any_sum(X, 2 ** j) + any_sum(2 ** j, Y)


def part_sum(i): # bin sum of [2**i, 2**(i+1))
    return (i+2) * 2 ** (i-1)


def solution(A, B):
    start = 2 ** math.floor(math.log2(A))
    return int(any_sum(start, B+1)) - int(any_sum(start, A))



# A, B = map(int, sys.stdin.readline().strip().split())

# print(solution(A, B))


def naive(A, B):
    result = 0
    for i in range(A, B+1):
        counter = bin(i).count("1")
        result += counter
    return result

for size in range(14, 16):
    print(size)
    for i in range(10**size-1000, 10 ** size-900):
        for j in range(i, 10 ** size):
            # print(i, j)
            # print(solution(i, j))
            # print(naive(i, j))
            assert solution(i, j) == naive(i, j), f"for {i}, {j}, result should be {naive(i,j)}, instead we got {solution(i, j)}"