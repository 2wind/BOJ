
def solution(N, dice_numbers):


    # 주사위가 1개일 경우 최대를 바닥으로 한 것이 답.
    if N == 1:
        print(sum(dice_numbers) - max(dice_numbers))
    else:
        # 한 면만 보이는 경우의 최솟값
        min1 = min(dice_numbers)

        # 두 이웃한 면이 보이는 경우의 최솟값
        # 경우는 12가지
        min_2s = [(0, 1), (0, 2), (0, 3), (0, 4),
                (1, 2), (1, 3), (2, 4), (3, 4),
                (1, 5), (2, 5), (3, 5), (4, 5)]
        min2 = min([dice_numbers[combo[0]] + dice_numbers[combo[1]] for combo in min_2s])

        # 세 이웃한 면이 보이는 경우의 최솟값
        # 경우는 8가지
        min_3s = [(0, 1, 2), (0, 2, 4), (0, 3, 4), (0, 1, 3),
                    (5, 1, 2), (5, 2, 4), (5, 3, 4), (5, 1, 3)]

        min3 = min([dice_numbers[combo[0]] + dice_numbers[combo[1]] + dice_numbers[combo[2]] for combo in min_3s])
            
        total_min = (N - 2) * (5*N - 6) * min1 + (8*N - 12) * min2 + 4 * min3
        print(total_min)


N = int(input())
dice_numbers = [int(x) for x in input().split()]
solution(N, dice_numbers)