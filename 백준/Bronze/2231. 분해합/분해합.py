n = input()
a = int(n) - len(n) * 9
b = int(n)

if a < 0:
    a = 0

for i in range(a, b):
    s = i + sum(map(int, str(i)))
    if s == int(n):
        print(i)
        break
    if i == b - 1:
        print(0)