X, K = map(int, input().split())


# Naive method for finding solution
def naive(X, K):
    nth = 0
    Y = 0
    while nth < K:
        Y += 1
        if X + Y == X | Y:
            print(bin(Y), bin(X|Y))
            nth += 1
        

    return Y


def math(X, K):
    checker_x = 1
    digit_K = 1
    finish = bin(K).count("1") - bin(X).count("1")


    if x & checker_x == 0:
        digit_K *= 2
    else:
        checker_x *= 2
    



print(naive(X, K))