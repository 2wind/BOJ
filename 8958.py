def calc(OX):
    scores = [0] * len(OX)
    
    prev = "X"
    for i in range(len(OX)):
        letter = OX[i]
        if letter == "O":
            if prev == "O":
                scores[i] = scores[i-1] + 1
            else:
                scores[i] = 1
        else:
            scores[i] = 0
          
        prev = letter
    return sum(scores)


N = int(input())
for i in range(N):
    ox_result = list(input())
    print(calc(ox_result))