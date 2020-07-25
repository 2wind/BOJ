def solver():
    word = input().upper()
    freq = {}
    for letter in list(word):
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1

    print(sorted(freq, key=(lambda x: x[1])))

solver()
    