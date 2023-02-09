from collections import Counter

i = iter(open(0))
n = int(next(i))
nums = sorted(list(map(int, i)))
print(round(sum(nums) / n))
print(nums[n // 2])
cnt = Counter(nums).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(nums[-1] - nums[0])