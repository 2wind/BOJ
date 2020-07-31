import sys

def quicksort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        key = numbers[0]
        numbers = numbers[1:]
        pos = 0
        keypos = 0
        while pos < len(numbers):
            number = numbers[pos]
            if number < key:
                numbers.insert(0, numbers.pop(pos))
                keypos += 1
            pos += 1
        numbers.insert(keypos, key)
        numbers[keypos+1:] = quicksort(numbers[keypos+1:])
        numbers[:keypos] = quicksort(numbers[:keypos])
        return numbers

def main():
    n = int(input())
    numbers = [sys.stdin.readline() for i in range(n)]
    numbers = [int(x) for x in numbers]
    [print(x) for x in quicksort(numbers)]

main()
testarray = [67, 5, 8, 24, 458, 100, 0]
assert(sorted(testarray) == quicksort(testarray))