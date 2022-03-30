from collections import defaultdict

N = int(input())
parents = [int(x) for x in input().split()]
# -1 0 0 1 1
#  0 1 2 3 4
removed = int(input())

# 그래프 생성
graph = defaultdict(list)
for i in range(-1, N):
    graph[i] = []

for idx, p in enumerate(parents):
    graph[p].append(idx)

# print(parents)
# print(graph)

# root = graph[-1]
# 재귀적으로 i 이하의 모든 원소를 제거
def remove(i):
    if i in graph:
        # i의 하위 원소에 대해 remove 호출
        for child in graph[i]:
            remove(child)

        # 이제 안전하게 i를 제거 가능
        graph.pop(i)

        


remove(removed)
# i의 부모에서도 i를 제거
if parents[removed] in graph:
    graph[parents[removed]].remove(removed)    

# print(graph)
# child가 없는 values의 갯수 count
count = 0
for k in graph.keys():
    v = graph[k]
    if k >= 0 and not v:
        count += 1

print(count)
