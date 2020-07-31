def word_sort(words):
    return sorted(sorted(words), key=len)

N = int(input())
words = set()
while N > 0:
    words.add(input())
    N -= 1
[print(word) for word in word_sort(list(words))]