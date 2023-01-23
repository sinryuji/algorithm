l = [-1 for _ in range(26)]
for i, c in enumerate(input()):
    if l[ord(c) - ord('a')] == -1:
        l[ord(c) - ord('a')] = i;
for i in l:
    print(i, end = ' ')