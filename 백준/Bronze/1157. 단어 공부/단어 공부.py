l = [0 for _ in range(26)]
str = input().upper()
for c in str:
    l[ord(c) - ord('A')] += 1
m = max(l)
cnt = 0
for i in l:
    if m == i:
        cnt += 1
if (cnt > 1):
    print('?')
else:
    print(chr(l.index(m) + ord('A')))