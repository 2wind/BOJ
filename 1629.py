
A, B, C = [int(i) for i in input().split()]

# print((A ** B) % C)

Bcopy = B
Bdiv = []
while Bcopy > 0:
    Bdiv.append(Bcopy % 2)
    Bcopy = Bcopy // 2

# print(Bdiv)
Bmult = []
multiplier = 1
index = 0
Bmult.append((A ** multiplier) % C)
while multiplier < B:
    Bmult.append((Bmult[index] ** 2) % C)
    multiplier = multiplier * 2
    index += 1

# print(Bmult)
leftover = 1
for i in Bmult:
    leftover = leftover * i
    
print(leftover % C)

