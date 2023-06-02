n, m = map(int, input().split())
t = list(map(int, input().split()))

def solution(t, m): 
    start = 1
    end = max(t)
    while start <= end:
        mid = (start + end) // 2
        cuts = 0
        for i in t:
            diff = i - mid
            if diff > 0:
                cuts += diff
        if cuts == m:
            return mid
        if cuts < m:
            end = mid - 1
        else:
            start = mid + 1

    return end
        
print(solution(t, m))