def binary_search(target, data):
    start = 0
    end = len(data) - 1
    
    while start < end:
        mid = (start + end) // 2
        if data[mid] >= target:
            end = mid
        else:
            start = mid + 1
    
    return start

def lis(data):
    dp = [1] * n
    s = [data[0]]
    
    for i in range(1, n):
        if s[-1] < data[i]:
            s.append(data[i])
        else:
            s[binary_search(data[i], s)] = data[i]
        dp[i] = len(s)
        
    return dp

n = int(input())
a = list(map(int, input().split()))
ret = 1

increase = lis(a)
decrease = lis(a[::-1])
decrease = decrease[::-1]

for i in range(n - 1):
    ret = max(ret, increase[i] + decrease[i] - 1)

print(ret)