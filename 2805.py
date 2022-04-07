N, M = [int(x) for x in input().split()]
trees = [int(x) for x in input().split()]
trees.sort()

def get_woods(trees, h):
    woods = 0
    for t in trees:
        woods += max(0, t - h)

    return woods

left, right = 0, max(trees)

height_max = -1

while left <= right:
    mid = (left + right) // 2

    woods = get_woods(trees, mid)

    if woods < M: # 나무를 덜 베었다면 범위를 앞쪽으로 줄여준다.
        right = mid - 1
    elif woods > M: # 나무를 더 베었다면 뒤쪽에서 좁혀준다.
        # 일단 최대 나무 높이를 갱신한다.
        height_max = max(height_max, mid)
        left = mid + 1
    else:
        # 나무 높이가 딱 알맞으므로 탐색을 종료한다.
        height_max = mid
        break

print(height_max)