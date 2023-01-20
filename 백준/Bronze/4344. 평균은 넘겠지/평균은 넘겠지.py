import sys

c = int(sys.stdin.readline())
for _ in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    n = l.pop(0)
    avg = sum(l) / len(l)
    cnt = 0
    for i in l:
        if i > avg:
            cnt += 1
    print(f"{cnt / n * 100:.3f}%")