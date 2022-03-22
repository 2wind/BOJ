def factorial(start, end = 1):
    number = 1
    for i in range(start, end, -1):
        number *= i
    return number

def nCk(N, K):
    return (factorial(N, K) // factorial(N - K, 1)) % 10007

[N, K] = [int(x) for x in input().split()]
print(nCk(N, K))