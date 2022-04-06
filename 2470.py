N = int(input())

solutions = sorted([int(x) for x in input().split()])

def find_solution_pair(solutions):

    left, right = 0, N-1
    best = [10000000000, None]

    while left < right:
        acidity = solutions[left] + solutions[right]

        if abs(acidity) < abs(best[0]):
            best[0] = acidity
            best[1] = (left, right)

        if acidity < 0:
            left += 1

        elif acidity > 0:
            right -= 1

        else:
            return (left, right)


    return best[1]

sols = find_solution_pair(solutions)
print(solutions[sols[0]], solutions[sols[1]])