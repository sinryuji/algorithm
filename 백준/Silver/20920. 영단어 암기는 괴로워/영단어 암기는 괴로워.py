import sys
input = sys.stdin.readline

n, m = map(int, input().split())
voca = dict()

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word not in voca:
        voca[word] = 1
    else:
        voca[word] += 1
sort = sorted(voca.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for i in sort:
  print(i[0])