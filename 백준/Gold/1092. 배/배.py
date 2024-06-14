import sys

input = sys.stdin.readline

N = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

ans = 0
if boxes[0] > cranes[0]:
    ans = -1
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        ans += 1

print(ans)