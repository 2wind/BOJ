A = int(input())
B = int(input())
C = int(input())
times = A * B * C
counter = [0] * 10
while times > 0:
    counter[times % 10] += 1
    times = times // 10
    
for i in counter:
    print(i)
