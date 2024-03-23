import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    d = [0] * (n + 1)

    for num in nums:
        d[num] += 1

    left = [i for i in range(1, n + 1) if not d[i]]

    for i in left:
        d[nums[i]] -= 1
        if d[nums[i]] == 0:
            left.append(nums[i])

    print(len(left))


T = int(input())
for _ in range(T):
    solve()
