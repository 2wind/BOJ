import sys
import itertools
import functools 

def get_part(paper, where):
    length = len(paper)
    side = int(length ** 0.5)
    x, y = where % 2, where // 2
    
    result = []
    for i in range(y * side // 2, (y + 1) * side // 2 ):
        for j in range(x * side // 2, (x + 1) * side // 2 ):
            result.append(paper[side * i + j])
            
    return result

def is_all_white(calc_result):
    if len(calc_result) == 1:
        return calc_result[0] == 0
    for i in range(4):
        if is_all_white(calc_result[i]):
            return False
    return True

def is_all_black(calc_result):
    if len(calc_result) == 1:
        return calc_result[0] == 1
    for i in range(4):
        if is_all_black(calc_result[i]):
            return False
    return True

def calc_paper(paper):
    length = len(paper)
    #side = int(length ** 0.5)
    if length == 1:
        return paper[0]

    first, second, third, fourth = get_part(paper, 0), get_part(paper, 1), get_part(paper, 2), get_part(paper, 3)
    result = [calc_paper(first), calc_paper(second), calc_paper(third), calc_paper(fourth)]
    if result == [0, 0, 0, 0]:
        result = 0
    elif result == [1, 1, 1, 1]:
        result = 1
    return result

def as_quadtree(result):
    if type(result) is int:
        return f"{result}"
    else:
        return f"({as_quadtree(result[0])}{as_quadtree(result[1])}{as_quadtree(result[2])}{as_quadtree(result[3])})"

n = int(input())
lists = []
for i in range(n):
    lists.append(sys.stdin.readline())
paper = list(itertools.chain.from_iterable([x.rstrip() for x in lists]))
paper = [int(x) for x in paper]
#print(paper)
result = calc_paper(paper)
print(as_quadtree(result))
#print(result)
