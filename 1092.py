import bisect

N = int(input())
cranes = sorted([int(x) for x in input().split()])
M = int(input())
boxes = sorted([int(x) for x in input().split()])
# 박스를 제거해야 할 위치인 indices
indices = [bisect.bisect(boxes, crane) -1 for crane in cranes]
# print(indices)
changed = True
time = 0

def calibrate(i):
    for j in range(i, -1, -1):
        while indices[j] >= 0 and boxes[indices[j]] < 0:
            indices[j] -= 1

# print(indices)
# print(boxes)

# 만약 가장 큰 크레인도 처리하지 못하는 상자가 있다면 처리 불가.
if indices[-1] < len(boxes)-1:
    print(-1)
else:
    # 직전에 변화가 있었다면 루프를 진행.
    while changed:
        changed = False
        # 만약 상자가 비어있다면 루프를 종료한다.
        if not boxes:
            break
        
        # 각 크레인에 대해, 큰 크레인부터,
        for i in range(N-1, -1, -1):
            # 크레인의 값 이하의 상자를 가져온다.
            # 이 때 값 이하의 상자 중 가장 큰 것을 선택한다.

            # 만약 box_index가 0보다 작다면 아무 일도 할 수 없다.
            if indices[i] < 0:
                continue

            # 만약 box_index 자리의 상자가 이미 제거되었다면, 제대로 된 위치로 이동시킨다.
            while indices[i] >= 0 and boxes[indices[i]] < 0:
                calibrate(i)

            # 만약 box_index가 0보다 작다면 아무 일도 할 수 없다.
            if indices[i] < 0:
                continue

            if cranes[i] >= boxes[indices[i]]: # 만약 크레인이 감당 가능하면
                boxes[indices[i]] = -1 # 상자를 처리한다.
                # 크레인 중 하나라도 처리가 가능했다면 변화가 있는 것이다.  
                changed = True
                indices[i] -= 1
            
        # 변화가 있었다면 시간을 1 높인다.
        # print(boxes)
        if changed: # 변화가 있었다면 시간을 진행
            time += 1
    # print(indices)

    print(time)


    