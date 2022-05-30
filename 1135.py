N = int(input())
tree = [int(x) for x in input().split()]
children_count = []
height_count = []

# 자식의 숫자가 많은 사람부터, 같다면 높이가 낮은 사람부터 전해야 한다.