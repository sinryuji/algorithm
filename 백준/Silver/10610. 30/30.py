N = input()

if '0' not in N:
    print(-1)
else:
    s = sum(map(int, N))
    if s % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(N, reverse=True)))