N = int(input())

# C++ 스럽게 작성한 순열 코드
def permutation(visited, arr, perm, depth):
    # 끝까지 도달한 경우
    if depth == len(perm):
        for i in range(depth-1):
            print(str(perm[i]) + " ", end="")
        print(perm[depth-1])

        return

    # 그렇지 않은 경우 arr에서 각 원소를 추가 시도함
    for i in range(len(arr)):
        # 방문한 경우 넘어감
        if visited[i]:
            continue

        # 방문 처리 (백트래킹)
        visited[i] = True
        # depth 자리에 대입함
        perm[depth] = arr[i]
        permutation(visited, arr, perm, depth+1) #depth를 하나 늘려서 방문
        visited[i] = False

R = N

permutation([False for _ in range(N)], list(range(1,N+1)), [None for _ in range(R)], 0)