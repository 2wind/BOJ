while True:
    edges = [int(x) for x in input().split()]
    edges.sort()
    [x, y, z] = edges
    if x == 0 and x == y and y == z:
        break
    elif x ** 2 + y ** 2 == z ** 2:
        print("right")
    else:
        print("wrong")