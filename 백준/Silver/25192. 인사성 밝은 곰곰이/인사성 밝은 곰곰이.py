import sys
input = sys.stdin.readline

n = int(input())
s = set()
ret = 0
for _ in range(n):
    chat = input().rstrip()
    if chat == "ENTER":
        ret += len(s)
        s = set()
    else:
        s.add(chat)
ret += len(s)
print(ret)