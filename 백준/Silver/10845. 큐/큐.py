import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
ret = []
for _ in range(n):
    cmd = input().rstrip()
    if cmd == 'pop':
        ret.append('-1' if len(q) == 0 else q.popleft())
    elif cmd == 'size':
        ret.append(str(len(q)))
    elif cmd == 'empty':
        ret.append('1' if len(q) == 0 else '0')
    elif cmd == 'front':
        ret.append('-1' if len(q) == 0 else q[0])
    elif cmd == 'back':
        ret.append('-1' if len(q) == 0 else q[-1])
    else:
        q.append(cmd.split()[1])
sys.stdout.write('\n'.join(ret))