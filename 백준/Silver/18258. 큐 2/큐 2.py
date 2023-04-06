import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    cmd = input().rstrip()
    if cmd == "pop":
        print(-1 if len(q) == 0 else q.popleft())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(1 if len(q) == 0 else 0)
    elif cmd == "front":
        print(-1 if len(q) == 0 else q[0])
    elif cmd == "back":
        print(-1 if len(q) == 0 else q[-1])
    else:
        q.append(int(cmd.split()[1]))