N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
answer = []
i = 0
    
while nums:
    i = (i + K - 1) % len(nums)
    answer.append(nums.pop(i))

print('<' + ', '.join(map(str, answer)) + '>')