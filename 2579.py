stairs = [0]
for _ in range(int(input())):
    stairs.append(int(input()))


# print(stairs)

# [2칸 이동시 점수, 1칸 이동시 점수]
score = [[0, 0] for _ in range(len(stairs))]

for i, stair in enumerate(stairs):
    # 0칸 (바닥), 1칸의 경우 stair의 값과 동일
    if i <= 1:
        score[i][0] = stair
        score[i][1] = stair
    else:
        # 2칸 이동하는 경우는 2계단 전, 2칸 이동시와 1칸 이동시 모두 가능
        score[i][0] = max(score[i-2]) + stair
        # 1칸 이동하는 경우는 1계단 전, 2칸 이동한 경우만 가능
        score[i][1] = score[i-1][0] + stair
    
# 마지막 칸에서의 최대 점수를 출력
print (max(score[-1]))