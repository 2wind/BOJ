from collections import deque


queue = deque()

p, q = [int(x) for x in input().split()]

answers = set()

step = 0

n = p

visited = set()

queue.append((n, step))


while len(queue) > 0:
    # print(queue)
    i, l = queue.popleft()
    # print(i, l)
    if (i == q):
        # print(f"{i}, {l}")
        answers.add(l)
        visited.add(i)
        continue
    if i < 0 or i > 100000 or i in visited:
        continue
    visited.add(i)
    if (i-1) not in visited:
        queue.append((i-1, l+1))
    if (i+1) not in visited:
        queue.append((i+1, l+1))
    if (i*2) not in visited:
        queue.appendleft((i*2, l))

print(min(answers))