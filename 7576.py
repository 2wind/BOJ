import copy

def simulate(tts):

    #find all 1s locations
    ones = []
    for i in range(N):
        for j in range(M):
            if tts[i][j] == 1:
                ones.append((i, j))

    #ripe nearby 0s
    # any_ripen = False

    days_after = -1

    zeroes = []
    # bfs instead of naive method

    print(ones)
    while ones:
        for coord in ones:
            if coord[0] > 0 and tts[coord[0]-1][coord[1]] == 0:
                tts[coord[0]-1][coord[1]] = 1
                zeroes.append((coord[0]-1, coord[1]))
                
            if coord[0] < N-1 and tts[coord[0]+1][coord[1]] == 0:
                tts[coord[0]+1][coord[1]] = 1
                zeroes.append((coord[0]+1, coord[1]))
            if coord[1] > 0 and tts[coord[0]][coord[1]-1] == 0:
                tts[coord[0]][coord[1]-1] = 1
                zeroes.append((coord[0], coord[1]-1))
            if coord[1] < M-1 and tts[coord[0]][coord[1]+1] == 0:
                tts[coord[0]][coord[1]+1] = 1
                zeroes.append((coord[0], coord[1]+1))

        days_after += 1
        print(tts)
        ones = zeroes
        zeroes = []
    
    #print(tts)
    if check_all_ripen(tomatoes):
        return days_after
    else:
        return -1
    # return any_ripen

def check_all_ripen(tomatoes):
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return False
    return True

M, N = [int(x) for x in input().split()]

tomatoes = []

for i in range(N):
    row = [int(x) for x in input().split()]
    tomatoes.append(row)

print(simulate(tomatoes))
#print(tomatoes)
# days_passed = 0
# while True:
#     if simulate(tomatoes):
#         days_passed += 1

#     else:
#         if check_all_ripen(tomatoes):
#             print(days_passed)
#         else:
#             print("-1")
#         break

