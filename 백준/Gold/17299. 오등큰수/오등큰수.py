import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = [0]
answer = [-1] * n
cnt = Counter(a)

for i in range(1, n):
    while s and cnt[a[s[-1]]] < cnt[a[i]]:
        answer[s.pop()] = a[i]
    s.append(i)
    
print(*answer)