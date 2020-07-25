def solver():
    N = int(input())
    remainder = N % 5
    if N in [4, 7]:
        print("-1")
    elif (remainder == 0): # 5
        print(N // 5)
    elif remainder == 1: # 6
        print(N // 5 + 1)
    elif remainder == 2: # 12(3*4)..
        print(N // 5 + 2)
    elif remainder == 3: # 3, 8...
        print(N // 5 + 1)
    else: # remainder == 4 
        print(N // 5 + 2)

        
solver()