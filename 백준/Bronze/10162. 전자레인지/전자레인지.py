T = int(input())
if T % 10 != 0:
    print(-1)
else:
    answer = []
    for s in [300, 60, 10]:
        answer.append(T // s)
        T %= s
    print(*answer)