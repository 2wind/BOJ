import sys

N, P = map(int, sys.stdin.readline().strip().split())


stack = []
numbers = set()
stack.append(N)
numbers.add(N)

while True:
    number = stack[-1]
    number = number * N % P
    if number in numbers:
        print(len(stack) - stack.index(number))
        break
    else:
        stack.append(number)
        numbers.add(number)