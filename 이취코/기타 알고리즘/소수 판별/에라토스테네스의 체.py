import math

n = 1000
array = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        for j in range(i * 2, n + 1, i):
            array[j] = False

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
