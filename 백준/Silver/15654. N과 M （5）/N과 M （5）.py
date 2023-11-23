import itertools

N, M = map(int, input().split())
nums = list(map(int, input().split()))

per = itertools.permutations(nums, M)
for i in list(sorted(per)):
    print(*i)