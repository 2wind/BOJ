from collections import deque

infix = list(input().strip())
postfix = []
pred = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
stack = deque()

for l in infix:
    if (65 <= ord(l) and ord(l) <= 90):
        postfix.append(l)
        # A to Z
    elif l == "(":
        stack.append(l)
    elif l == ")":
        while len(stack) > 0 and stack[-1] != "(":
            postfix.append(stack.pop())
        stack.pop()

    else:

        if len(stack) == 0 or stack[-1] == "(" or pred[stack[-1]] < pred[l]:
            stack.append(l)
        else:
            while len(stack) > 0 and pred[stack[-1]] >= pred[l]:
                postfix.append(stack.pop())
            stack.append(l)

    
stack.reverse()

print(f"{''.join(postfix)}{''.join(stack)}")