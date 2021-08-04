def calc(n):
    if n < 4:
        return [0, 1, 2, 4][n]
    else:
        return calc(n-1) + calc(n-2) + calc(n-3)


T = int(input())
for k in range(T):
    print(calc(int(input())))