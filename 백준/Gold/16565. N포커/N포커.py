from math import comb

N = int(input())
mod = 10007

answer = 0
for i in range(1, N // 4 + 1):
    val = (comb(13, i) * comb(52 - (4 * i), N - (4 * i)))
    if i % 2:
        answer += val % mod
    else:
        answer -= val % mod

print(answer % mod)
