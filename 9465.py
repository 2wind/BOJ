# storage: [(max_value, up), ... , False, False] (len(storage) == n)
def calc_value(first, second, k, storage):
    st_value = storage[k]
    f, s = first[k], second[k]
    if st_value:
        return storage[n]
    elif k == 0:
        storage[k] = (f, True) if f > s else (s, False)        
        return storage[k]
    elif k == 1:
        last = calc_value(first, second, 0, storage)


        return storage[k]
    else:
        k_minus_1, k_minus_2 = storage[k-1], storage[k-2]

        storage[k] = 1 # calculated value





def pick_and_solve(up, first, second, n, storage):
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
    solve(first_line, second_line, n - 1)