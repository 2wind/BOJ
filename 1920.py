N = int(input())
numbers = set([int(i) for i in input().split()])
M = int(input())
inputs = [int(i) for i in input().split()]

for i in inputs:
    print("1") if i in numbers else print("0")
   
