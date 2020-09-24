A, B, C = [int(x) for x in input().split()]

#assert(A ** B % C
#   == (A % C) ** B % C)
result = 1
while B:
    if B % 2 == 1:
        result = result * A % C
    B = B // 2
    A = A ** 2 % C
print(result)

print(pow(A, B, C))
#result = 1
#while True:
    
#    A = A * A % C
#print(N % C)
#print((A % C) ** B % C)