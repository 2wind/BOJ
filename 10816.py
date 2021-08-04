from collections import deque
N = int(input())

numbers = [int(x) for x in input().split()]
deck = {}

for number in numbers:
    if number not in deck:
        deck.update({number: 1})
    else:
        deck.update({number: deck[number]+1})\



M = int(input())

guesses = [int(x) for x in input().split()]
result = deque()
for guess in guesses:
    if guess not in deck:
        result.append("0")
    else:
        result.append(str(deck[guess]))

print(" ".join(result))