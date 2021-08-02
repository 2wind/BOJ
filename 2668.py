import sys

N = int(sys.stdin.readline().strip())
numbers = [0 for i in range(N+1)]
for i in range(1, N+1):
    n = int(sys.stdin.readline().strip())
    numbers[i] = n

visited = [False for i in range(N+1)]
cycles = []


for i in range(1, N+1):
    if not visited[i]:
        stack = [i]
        while stack:
            # print(stack)
            number = stack[-1]
            if visited[number]: 
                # print("cycle: ", stack[stack.index(number):-1])
                cycles += stack[stack.index(number):-1]
                break
            else:
                visited[number] = True
                linked = numbers[number]
                stack.append(linked)

print(len(cycles))
cycles.sort()
for n in cycles:
    print(n)