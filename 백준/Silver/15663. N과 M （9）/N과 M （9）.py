N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
temp = []
visited = [False] * N

def dfs():
    if len(temp) == M:
        print(*temp)
        return
    remember_me = 0
    for i in range(N):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()