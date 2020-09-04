n = int(input())
cases = [1, 1] + [-1] * (n-1)

for i in range(2, n+1):
    cases[i] = (cases[i-1] + cases[i-2] * 2) % 10007

print(cases[n])