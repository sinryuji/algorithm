def isGroup(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1] and s[i] in s[i + 1:]:
            return False
    return True

n = int(input())
ret = 0
for _ in range(n):
    if isGroup(input()):
        ret += 1
print(ret)