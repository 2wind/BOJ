N = int(input())
numbers = [int(x) for x in input().split()]
minimum = 10000000
maximum = -10000000
for i in range(N):
    number = numbers[i]
    if number < minimum:
        minimum = number
    if maximum < number:
        maximum = number
print("{0} {1}".format(minimum, maximum))