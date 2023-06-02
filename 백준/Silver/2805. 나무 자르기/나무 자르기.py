import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
t = Counter(map(int, input().split()))

start = 1
end = max(t)
while start <= end:
    mid = (start + end) // 2
    cuts = sum((h - mid) * i for h, i in t.items() if h > mid)
    if cuts < m:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)