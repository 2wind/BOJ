n = int(input())

sol = [["1"] for x in range(n+1)]
sol[0] = None

for i in range(1, n+1):
    sol1, sol2, sol3 = None, None, None
    if i % 2 == 0:
        sol2 = sol[i//2]

    if i % 3 == 0:
        sol3 = sol[i//3]
    
    if i > 1:
        sol1 = sol[i-1]

    m = None
    
    if sol1 is not None:
        m = sol1
    if sol2 is not None and len(sol2) < len(m):
        m = sol2
    if sol3 is not None and len(sol3) < len(m):
        m = sol3
    if m is not None:
        sol[i] = [str(i)] + m

print(len(sol[n]) -1)
print(" ".join(sol[n]))
