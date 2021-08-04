n = int(input())
coords = [int(x) for x in input().split()]
sorted_coords = sorted(set(coords))
correspond = {}
for i in range(len(sorted_coords)):
    correspond[sorted_coords[i]] = i
#print(sorted_coords)
#print(correspond)
result = []
for j in range(n): 
    result.append(str(correspond[coords[j]]))

print(" ".join(result))