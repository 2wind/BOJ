import sys

N = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
numbers.sort()


best = (3000000000, None)

def find_best(a, b, c):
    diff = abs(a+b+c)
    if diff < best[0]:
        return (diff, (a, b, c))
    else:
        return best

zero_found = False

for i in range(N-2):
    if zero_found:
        break
    k = i+1
    j = N-1
    while k < j: 
        best  = find_best(numbers[i], numbers[k], numbers[j])
        sum_3 = numbers[i] + numbers[k] + numbers[j]
        if sum_3 > 0:
            j -= 1
        elif sum_3 == 0:
            print(f"{best[1][0]} {best[1][1]} {best[1][2]}")
            zero_found = True
            break
        else:
            k += 1

if not zero_found:
    print(f"{best[1][0]} {best[1][1]} {best[1][2]}")