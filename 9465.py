def pick_and_solve(up, first, second, n):
    if n == 0:
        return first[0] if up else second[0]
    else:
        if up:
            return first[n] + max(pick_and_solve(False, first, second, n-1), pick_and_solve(False, first, second, n-2))
        else:
            return second[n] + max(pick_and_solve(True, first, second, n-1), pick_and_solve(True, first, second, n-2))
def solve(first, second, n):
    return max(pick_and_solve(True, first, second, n), pick_and_solve(False, first, second, n))

T = int(input())
for i in range(T):
    n = int(input())
    first_line, second_line = [int(x) for x in input().split()], [int(x) for x in input().split()]
    line = [(x, y) for x in first_line for y in second_line]
    last_pick_x = None
    sticker = 0
    for i in range(n % 2, n, 2):
        selection = line[:i]
        if not selection:
            continue
        elif i == 1:
            x, y = selection[0]
            last_pick_x = True if x > y else False
            sticker = max(x, y)
        else:
            curr = selection[-2:]
            if last_pick_x:
                c1, c2 = curr[0][1] + curr[1][0], curr[1][1]
                last_pick_x = True if c1 > c2 else False
                add_value = max(c1, c2)
            else:
                c1, c2 = curr[0][0] + curr[1][1], curr[0][1]
                last_pick_x = True if c1 < c2 else False
                add_value = max(c1, c2)
            sticker = sticker + add_value

    print(sticker)
        


        