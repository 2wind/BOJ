import math


def solver():
    input_list = input().split()
    A, B, C = int(input_list[0]), int(input_list[1]), int(input_list[2])
    if B >= C or (C - B) * 2100000000 < A  :
        print("-1")
    else:
        n = A / (C - B) 
        print (math.floor(n) + 1)
    
    
solver()