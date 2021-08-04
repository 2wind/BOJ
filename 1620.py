import sys

n, m = [int(x) for x in input().split()]

pokeDex = {}
pokeDexReverse = {}
result = []
for i in range(n):
    pokemon = sys.stdin.readline().strip()
    pokeDex[i+1] = pokemon
    pokeDexReverse[pokemon] = str(i+1)
for j in range(m):
    cmd = sys.stdin.readline().strip()
    if cmd.isdigit():
        result.append(pokeDex[int(cmd)])
    else:
        result.append(pokeDexReverse[cmd])
print("\n".join(result))

