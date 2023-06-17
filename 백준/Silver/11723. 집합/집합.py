import sys
input = sys.stdin.readline

m = int(input())
s = set()
s_all = set([str(i) for i in range(1, 21)])

for _ in range(m):
    cmd = list(input().split())
    if cmd[0] == "all":
        s = s_all
    elif cmd[0] == "empty":
        s = set()
    elif cmd[0] == "add":
        s.add(cmd[1])
    elif cmd[0] == "remove":
        s.discard(cmd[1])
    elif cmd[0] == "check":
        sys.stdout.write("1\n" if cmd[1] in s else "0\n")
    elif cmd[0] == "toggle":
        if cmd[1] in s: s.discard(cmd[1])
        else: s.add(cmd[1])