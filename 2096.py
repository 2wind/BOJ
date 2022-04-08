
N = int(input())

scores_max = []
scores_min = []
for _ in range(N):
    num = [int(x) for x in input().split()]
    num2 = num[:]
    if scores_max:
        num[0] += max(scores_max[0], scores_max[1])
        num[1] += max(scores_max)
        num[2] += max(scores_max[1], scores_max[2])
    scores_max = num

    if scores_min:
        num2[0] += min(scores_min[0], scores_min[1])
        num2[1] += min(scores_min)
        num2[2] += min(scores_min[1], scores_min[2])
    scores_min = num2


print(max(scores_max))
print(min(scores_min))
