import sys

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == i:
            break
        elif cards[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if start <= end:
        sys.stdout.write("1 ")
    else:
        sys.stdout.write("0 ")