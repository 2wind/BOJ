import heapq


N = int(input())
schedules = []
for _ in range(N):
    _, i, j = [int(x) for x in input().split()]
    schedules.append([i, j])

# 시작 시간이 이른 것부터 평가
schedules.sort(key=lambda x: x[0])

new_schedules = []

# 각 스케줄에 대해
for schedule in schedules:
    i, j = schedule
    # 종료 시간보다 현재 시작 시간이 뒤에 있다면 병합 가능
    if new_schedules and new_schedules[0][0] <= i:
        # 하나를 꺼내고
        new_schedule = heapq.heappop(new_schedules)
        # 종료 시간을 병합
        new_schedule[0] = max(new_schedule[0], j)
        # 그 뒤 적절하게 다시 넣어준다.
        heapq.heappush(new_schedules, new_schedule)
    else:
        # 종료 시간이 이른 것이 먼저 오도록 삽입
        heapq.heappush(new_schedules, schedule[::-1])

    # print(new_schedules)

print(len(new_schedules))
