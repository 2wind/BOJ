from collections import deque

N = int(input())

board = [[0 for j in range(N)] for i in range(N)]

def check_v(vset, i, j):
    if i in vset:
        return False

    return True

def check_diag(ldiag, rdiag, i, j):
    if i+j in ldiag:
        return False

    if i-j+N-1 in rdiag:
        return False
    return True

def place(i, queens, count, notcol, ldiag, rdiag, vset):
    if queens < N:
        for j in notcol:
            if check_v(vset, i, j) and check_diag(ldiag, rdiag, i, j):
                if i == N-1:
                    count = count + 1
                    return count
                else:
                    nc = notcol.copy()
                    ldiag.add(i+j)
                    rdiag.add(i-j+N-1)
                    nc.remove(j)
                    vset.add(i)
                    count = place(i+1, queens+1, count, nc, ldiag, rdiag, vset)
                    vset.remove(i)
                    ldiag.remove(i+j)
                    rdiag.remove(i-j+N-1)
                    continue               
        return count
    else:
        count = count + 1
        return count


result = place(0, 0, 0, set(range(N)), set(), set(), set())

print(result)
