import sys

n = int(input())
numbers = [sys.stdin.readline() for i in range(n)]
for i in numbers:
    [a, b] = [int(x) for x in i.split()]
    print(a + b)
