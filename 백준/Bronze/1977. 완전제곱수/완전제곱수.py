import math

M = int(input())
N = int(input())

min_ = math.ceil(M ** 0.5)
max_ = math.ceil(N ** 0.5)
if N != max_ ** 2:
    max_ -= 1

if min_ >= max_:
    print(-1)
else:
    answer = 0
    for i in range(min_, max_ + 1):
        answer += i ** 2
    print(answer)
    print(min_ ** 2)