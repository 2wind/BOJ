def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

def LCM(n, m):
    return n * m // GCD(n, m)
def GCD(n, m):
    div_of_n, div_of_m = set(divisors(n)), set(divisors(m))
    return max(div_of_m & div_of_n)

[N, M] = [int(x) for x in input().split()]
print(GCD(N, M))
print(LCM(N, M))