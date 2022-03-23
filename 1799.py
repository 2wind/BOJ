N = int(input())
# 체스보드 설정
# 체스를 놓을 수 있는 곳
chess_board = [[0 for _ in range(N)] for _ in range(N)]
# 오른쪽 대각선이 동일한 곳
chess_diffs = chess_board[:]
# 왼쪽 대각선이 동일한 곳
chess_sums = chess_board[:]

for row in range(N):
    chess_board[row] = [int(x) for x in input().split()]
    chess_diffs[row] = list(range(row,row-N,-1))
    chess_sums [row] = list(range(row,row+N))

# print(chess_board)
# print(chess_diffs)
# print(chess_sums)



def dfs(i, j, visited):
    if i < 0 or i >= N or j < 0 or j >= N:
        return len(visited)
    if chess_board[i][j] == 0:
        i, j = i + ((j+1) // N), (j+1) % N
        n = dfs(i, j, visited)
        return n
    for v in visited:
        if chess_diffs[v[0]][v[1]] == chess_diffs[i][j] or chess_sums[v[0]][v[1]] == chess_sums[i][j]:
            i, j = i + ((j+1) // N), (j+1) % N
            n = dfs(i, j, visited)
            return n

    new_visited = visited[:]
    new_visited.append((i, j))
    i, j = i + ((j+1) // N), (j+1) % N
    n = dfs(i, j, new_visited)
    new_visited.pop()
    return n

print(dfs(0, 0, []))
