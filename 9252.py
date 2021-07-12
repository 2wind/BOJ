from collections import deque

A = input()
B = input()

LCS = [[0 for x in range(len(B)+1)] for y in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])

i = len(A)
j = len(B)
st = deque()
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        st.appendleft(A[i-1])
        i = i-1
        j = j-1
    elif LCS[i-1][j] > LCS[i][j-1]:
        i = i-1
    else:
        j = j-1

print("".join(st).strip())