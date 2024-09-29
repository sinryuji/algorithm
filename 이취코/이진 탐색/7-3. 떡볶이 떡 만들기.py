N, M = map(int, input().split())

array = list(map(int, input().split()))

start, end = 0, max(array)

answer = 0
while start <= end:
    mid = (start + end) // 2

    print('mid:', mid)

    total = 0
    for n in array:
        if n > mid:
            total += n - mid

    print(total)

    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)