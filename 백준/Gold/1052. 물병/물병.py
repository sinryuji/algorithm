N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    s = bin(N)[::-1].index('1')
    N += 2 ** s
    answer += 2 ** s

print(answer)