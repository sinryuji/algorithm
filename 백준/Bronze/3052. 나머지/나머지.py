l = [int(input()) for _ in range(10)]
s = set()
for i in l:
    s.add(i % 42)
print(len(s))