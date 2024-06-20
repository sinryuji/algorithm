import sys

input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
pos = []
neg = []

for book in books:
    if book > 0:
        pos.append(book)
    else:
        neg.append(abs(book))

pos.sort(reverse=True)
neg.sort(reverse=True)

max_ = max(pos[0] if pos else 0, neg[0] if neg else 0)
result = 0

for i in range(0, len(pos), M):
    result += pos[i] * 2
for i in range(0, len(neg), M):
    result += neg[i] * 2

print(result - max_)