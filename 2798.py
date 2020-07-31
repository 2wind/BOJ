def solver():
    N, M = [int(x) for x in input().split()]
    cards = [int(x) for x in input().split()]
    cards.sort(reverse=True)
    max_value = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                result = cards[i] + cards[j] + cards[k] 
                if result == M :
                    print(result)
                    return
                elif result < M and max_value < result:
                    max_value = result
    print(max_value)

solver()