import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ret = []
d = deque()
for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'pop_front':
        ret.append('-1' if len(d) == 0 else d.popleft())
    elif cmd[0] == 'pop_back':
        ret.append('-1' if len(d) == 0 else d.pop())
    elif cmd[0] == 'size':
        ret.append(str(len(d)))
    elif cmd[0] == 'empty':
        ret.append('1' if len(d) == 0 else '0')
    elif cmd[0] == 'front':
        ret.append('-1' if len(d) == 0 else d[0])
    elif cmd[0] == 'back':
        ret.append('-1' if len(d) == 0 else d[-1])
    elif cmd[0] == 'push_back':
        d.append(cmd[1])
    else:
        d.appendleft(cmd[1])
sys.stdout.write('\n'.join(ret))