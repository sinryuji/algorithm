import sys

input = sys.stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])

i = 0
ans = 0
latest_end = (3, 1)

while i < N:
    sm, sd, em, ed = arr[i]
    if (sm, sd) <= latest_end <= (em, ed):
        max_end = (em, ed)
        while i < N - 1:
            nsm, nsd, nem, ned = arr[i + 1]
            if latest_end < (nsm, nsd):
                break
            if max_end < (nem, ned):
                max_end = (nem, ned)
            i += 1

        ans += 1
        latest_end = max_end

        if (11, 30) < latest_end:
            print(ans)
            break
    i += 1
else:
    print(0)