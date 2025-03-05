N = int(input())
s = input()
for _ in range(N-1):
    tmp = input()
    new = ''
    for i in range(len(s)):
        if s[i] != '?' and s[i] != tmp[i]:
            new += '?'
        else:
            new += s[i]
    s = new
print(s)