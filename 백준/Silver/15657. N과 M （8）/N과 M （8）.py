N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return
    for i in range(start, N):
        temp.append(nums[i])
        dfs(i)
        temp.pop()

dfs(0)