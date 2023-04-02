import sys
input = sys.stdin.readline

n = int(input())
rainbow = set(["ChongChong"])
for _ in range(n):
    a, b = input().split()
    if a in rainbow:
        rainbow.add(b)
    elif b in rainbow:
        rainbow.add(a)
print(len(rainbow))