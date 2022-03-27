N = int(input())
letters = []
for _ in range(N):
    letters.append(input())

def compare_letters(p, q):
    if p == q:
        return 0
    if p+1 == q and letters[p] == letters[q]:
        return 0

    if letters[p] < letters[q]:
        return -1
    if letters[p] > letters[q]:
        return 1
    else:
        return compare_letters(p+1, q-1)


result = []
i, j = 0, N-1
count = 0

while i <= j:
    
    if count > 0 and count % 80 == 0:
        result.append("\n")
        
    if letters[i] < letters[j]:
        result.append(letters[i])
        i += 1
    elif letters[i] > letters[j]:
        result.append(letters[j])
        j -= 1
    else:
        # compare letters recursively until different or hit end
        comp = compare_letters(i,j)
        if comp <= 0:
            result.append(letters[i])
            i += 1
        else:
            result.append(letters[j])
            j -= 1


    count += 1

print("".join(result).strip())