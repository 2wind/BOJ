# G == W ** 2 - M ** 2
# 15 = 4 ** 2 - 1 ** 2
# 15 = 8 ** 2 - 7 ** 2
G = int(input())

# sqrt(G + m ** 2) => w_c
# if w_c == int(w_c): possible
# too many cases

# two pointer solution

i, j = 1, 1
sol = []

while j <= G:
    s = j ** 2 - i ** 2

    if s == G:
        sol.append(str(j))
        i += 1
        j += 1

    elif s > G:
        i += 1
    
    else:
        j += 1

if not sol:
    print("-1") 
else:
    print("\n".join(sol))