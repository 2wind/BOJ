import sys
import copy

N = int(sys.stdin.readline().strip())

board = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))


# direction: U, D, L, R
def move(board, direction):

    max_number = -1
    stack = []

    if direction == 0:
        for i in range(N):
            result = []
            for j in range(N):
                current = board[j][i]
                if current == 0:
                    continue
                elif not stack:
                    stack.append(current)
                elif stack[-1] == current:
                    stack[-1] += current
                    result.append(stack.pop())
                else:
                    result.append(stack.pop())
                    stack.append(current)

            if stack:
                result.append(stack.pop())
            if result and max(result) > max_number:
                max_number = max(result)
            if len(result) < N:
                result += [0] * (N-len(result))
            for j in range(N):
                board[j][i] = result[j]
    elif direction == 1:
        for i in range(N):
            result = []
            for j in range(N-1, -1, -1):
                current = board[j][i]
                if current == 0:
                    continue
                elif not stack:
                    stack.append(current)
                elif stack[-1] == current:
                    stack[-1] += current
                    result.append(stack.pop())
                else:
                    result.append(stack.pop())
                    stack.append(current)

            if stack:
                result.append(stack.pop())
            if result and max(result) > max_number:
                max_number = max(result)
            if len(result) < N:
                result += [0] * (N-len(result))
            result.reverse()
            for j in range(N-1, -1, -1):
                board[j][i] = result[j]
    elif direction == 2:
        for i in range(N):
            result = []
            for j in range(N):
                current = board[i][j]
                if current == 0:
                    continue
                elif not stack:
                    stack.append(current)
                elif stack[-1] == current:
                    stack[-1] += current
                    result.append(stack.pop())
                else:
                    result.append(stack.pop())
                    stack.append(current)
            if result and max(result) > max_number:
                max_number = max(result)
            if stack:
                result.append(stack.pop())
            if len(result) < N:
                result += [0] * (N-len(result))
            for j in range(N):
                board[i][j] = result[j]
    else:
        for i in range(N):
            result = []
            for j in range(N-1, -1, -1):
                current = board[i][j]
                if current == 0:
                    continue
                elif not stack:
                    stack.append(current)
                elif stack[-1] == current:
                    stack[-1] += current
                    result.append(stack.pop())
                else:
                    result.append(stack.pop())
                    stack.append(current)
            if result and max(result) > max_number:
                max_number = max(result)
            if stack:
                result.append(stack.pop())
            if len(result) < N:
                result += [0] * (N-len(result))
            result.reverse()
            for j in range(N-1, -1, -1):
                board[i][j] = result[j]
    return board, max_number

def play(board, direction, number):
    # print(f"direction:{direction}, depth:{number}")
    moved, max_size = move(board, direction)
    # print(moved)
    if number >= 4:
        return max_size
    else:
        u = play(copy.deepcopy(moved), 0, number+1)
        d = play(copy.deepcopy(moved), 1, number+1)
        l = play(copy.deepcopy(moved), 2, number+1)
        r = play(copy.deepcopy(moved), 3, number+1)
        return(max(u, d, l, r))

print(max(play(copy.deepcopy(board), 0, 0), play(copy.deepcopy(board), 1, 0), play(copy.deepcopy(board), 2, 0), play(copy.deepcopy(board), 3, 0)))

