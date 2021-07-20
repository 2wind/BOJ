import sys
import math

def ccw(dot1, dot2, dot3):
    S = (dot2[0] - dot1[0]) * (dot3[1] - dot1[1]) - (dot2[1] - dot1[1]) * (dot3[0] - dot1[0])

    return 0 if math.isclose(S, 0) else 1 if S > 0 else -1

def isbetween(dot1, dot2, compared):
    (big_x, small_x) = (dot1[0], dot2[0]) if (dot1[0] > dot2[0]) else (dot2[0], dot1[0])
    (big_y, small_y) = (dot1[1], dot2[1]) if (dot1[1] > dot2[1]) else (dot2[1], dot1[1])
    return small_x <= compared[0] and compared[0] <= big_x and small_y <= compared[1] and compared[1] <= big_y
        

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

result1 = ccw((x3, y3), (x4, y4), (x1, y1))
result2 = ccw((x3, y3), (x4, y4), (x2, y2))
result3 = ccw((x1, y1), (x2, y2), (x3, y3))
result4 = ccw((x1, y1), (x2, y2), (x4, y4))

cross1 = result1 * result2
cross2 = result3 * result4
if cross1 == 0 and cross2 == 0:
    if isbetween((x1, y1), (x2, y2), (x3, y3)) or isbetween((x1, y1), (x2, y2), (x4, y4)):
        print(1)
    else:
        print(0)
elif cross1 <= 0 and cross2 <= 0:
    print(1)
else:
    print(0)
