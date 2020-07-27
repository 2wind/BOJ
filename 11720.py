def summation(numbers):
    if len(numbers) == 1:
        return int(numbers[0])
    n = numbers[0]
    rest = numbers[1:]
    return int(n) + summation(rest)

N = int(input())
numbers = list(input())
print(summation(numbers))