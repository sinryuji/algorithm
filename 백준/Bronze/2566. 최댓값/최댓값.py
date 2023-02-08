maxVal = 0
x = 0
y = 0
for i in range(1, 10):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] >= maxVal:
            maxVal = l[j]
            x = i
            y = j + 1
print(maxVal)
print(x, y)