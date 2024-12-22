def cal(level, diffs, times):
    result = 0
        
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        if diff <= level:
            result += time_cur
        else:
            time_prev = times[i - 1]
            result += (diff - level) * (time_cur + time_prev) + time_cur
    
    return result

def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        
        total = cal(mid, diffs, times)
        if total <= limit:
            right = mid - 1
        else:
            left = mid + 1
            
    return left