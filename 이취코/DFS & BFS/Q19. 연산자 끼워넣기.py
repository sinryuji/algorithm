# https://www.acmicpc.net/problem/14888

def dfs(x, total, plus, minus, mul, div):
    global maximum, minimum
    if x == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
    if plus:
        dfs(x + 1, total + nums[x], plus - 1, minus, mul, div)
    if minus:
        dfs(x + 1, total - nums[x], plus, minus - 1, mul, div)
    if mul:
        dfs(x + 1, total * nums[x], plus, minus, mul - 1, div)
    if div:
        dfs(x + 1, int(total / nums[x]), plus, minus, mul, div - 1)


n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9
dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
