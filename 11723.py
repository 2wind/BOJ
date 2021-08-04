import sys

def parseCommand(S, cmd):
    cmd = cmd.strip()
    if cmd == "empty":
        S = set()
    elif cmd == "all":
        S = set(range(1, 21, 1))
    else:
        cmd_main, num = cmd.split()[0], int(cmd.split()[1])
        if cmd_main == "add" and num not in S:
            S.add(num) 
        elif cmd_main == "remove" and num in S:
            S.remove(num)
        elif cmd_main == "toggle":
            S.remove(num) if num in S else S.add(num)
        elif cmd_main == "check":
            print("1") if num in S else print("0")
        else:
            pass
    return S



def main():
    m = int(input())
    S = set()
    for i in range(m):
        S = parseCommand(S, sys.stdin.readline())


main()