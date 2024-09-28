import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
seq = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if seq[0] == seq[1]:
        print(seq[0])
    else:
        print('A')
else:
    if seq[1] - seq[0] == 0:
        a = 0
    else:
        a = (seq[2] - seq[1]) // (seq[1] - seq[0])
    b = seq[1] - seq[0] * a

    answer = seq[-1] * a + b
    for i in range(N - 1):
        if seq[i] * a + b != seq[i + 1]:
            answer = 'B'
            break

    print(answer)