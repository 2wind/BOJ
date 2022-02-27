N = int(input())
coords = []
for _ in range(N):
    coord = [int(x) for x in input().split()]
    coords.append(coord)
coords.sort(key=lambda x: x[1])
coords.sort(key=lambda x: x[0])

for c in coords:
    print(f"{c[0]} {c[1]}")