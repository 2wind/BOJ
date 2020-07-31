def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def nCk(N, K):
    return int(factorial(N) // (factorial(K) * factorial(N - K)))

[N, K] = [int(x) for x in input().split()]
print(nCk(N, K))