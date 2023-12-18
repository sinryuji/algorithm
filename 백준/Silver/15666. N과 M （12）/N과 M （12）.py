import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))
N = len(nums)
temp = []

def dfs():
    if len(temp) == M:
        print(*temp)
        return
    for i in range(N):
        if not temp or nums[i] >= temp[-1]:
            temp.append(nums[i])
            dfs()
            temp.pop()
    
dfs()