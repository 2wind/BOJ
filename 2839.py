def solver():
    N = int(input())
    five_grams = N // 5
    three_grams = (N - five_grams * 5) // 3
    if N - five_grams * 5 - three_grams * 3 != 0:
        print("-1")
    else:
        print(five_grams + three_grams)
        
solver()