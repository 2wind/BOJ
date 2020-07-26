N = int(input())
Ns = [int(x) for x in input().split()]
max_number = max(Ns)
new_Ns = [x / max_number * 100 for x in Ns]
print(sum(new_Ns) / N)