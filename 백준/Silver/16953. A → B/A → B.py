A, B = map(int, input().split())
cnt = 1

while B > A:
    if B % 10 == 1:
        B //= 10
    else:
        B /= 2
    cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)