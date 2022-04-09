L, C = [int(x) for x in input().split()]

letters = input().split()
letters.sort()

# L개의 알파벳을 뽑는다. 이 때 적어도 1개의 모음과 적어도 2개의 모음을 뽑아야 한다.

def combination(arr, comb, index, depth, vowel, cons):
    if depth == len(comb) and any(comb) is not None :
        if vowel >= 1 and cons >= 2:
            print("".join(comb))

        return
    

    for i in range(index, len(arr)):
        comb[depth] = arr[i]
        if arr[i] in ('a', 'e', 'i', 'o', 'u'):
            v, c = 1, 0
        else:
            v, c = 0, 1

        combination(arr, comb, i+1, depth+1, vowel+v, cons+c)

combination(letters, [None for _ in range(L)], 0, 0, 0, 0)