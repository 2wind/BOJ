[n, k] = [int(x) for x in input().split()]

josephus = list(range(1, n+1, 1))
pos = 0
result = []
while len(josephus) > 0:
    pos = (pos - 1 + k) % len(josephus)
    result.append(josephus.pop(pos))
    
result = [str(x) for x in result]
print("<" + ", ".join(result) + ">")