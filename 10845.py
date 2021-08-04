from collections import deque
import sys

Q = deque()

N = int(sys.stdin.readline().strip())

for i in range(N):
    cmd = sys.stdin.readline().strip()

    if (cmd.startswith("push")):
        Q.append(cmd.split()[1])
        continue
    elif (cmd == "pop"):
        if len(Q) > 0:
            sys.stdout.write(Q.popleft())
        else:
            sys.stdout.write("-1")
        
    elif cmd == "size":
        sys.stdout.write(str(len(Q)))
    elif cmd == "empty":
        if len(Q) > 0:
            sys.stdout.write("0")
        else:
            sys.stdout.write("1")
    elif cmd == "front":
        if len(Q) > 0:
            sys.stdout.write(Q[0])
        else:
            sys.stdout.write("-1")
    elif cmd == "back":
        if len(Q) > 0:
            sys.stdout.write(Q[-1])
        else:
            sys.stdout.write("-1")
    else:
        raise Exception()
    sys.stdout.write("\n")