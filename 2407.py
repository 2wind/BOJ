import functools
import operator

n, m = [int(x) for x in input().split()]

# nCm
# n! / {m! * (n-m)!}

upper = list(range(n-m +1, n+1, 1))
lower = list(range(1, m+1, 1))

print(functools.reduce(operator.mul, upper) // functools.reduce(operator.mul, lower))