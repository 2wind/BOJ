notes = [int(x) for x in input().split()]
if notes == sorted(notes):
    print("ascending")
elif notes == sorted(notes, reverse=True):
    print("descending")
else:
    print("mixed")