magic_number = 1000000007

def fib(n):
    matrix = [[1, 1], [1, 0]]
    if n < 2:
        return n


    power(matrix, n-1)

    return matrix[0][0] % magic_number

def dot(M, N):
    x = (M[0][0] * N[0][0] + M[0][1] * N[1][0]) % magic_number
    y = (M[0][0] * N[0][1] + M[0][1] * N[1][1]) % magic_number
    z = (M[1][0] * N[0][0] + M[1][1] * N[1][0]) % magic_number
    w = (M[1][0] * N[0][1] + M[1][1] * N[1][1]) % magic_number

    M[0][0], M[0][1], M[1][0], M[1][1] = x, y, z, w


def power(matrix, n):
    if n < 2:
        return
    M = [[1, 1], [1, 0]]

    power(matrix, n // 2)
    dot(matrix, matrix)

    if (n%2 == 1):
        dot(matrix, M)


i = int(input())
print(fib(i))
    
