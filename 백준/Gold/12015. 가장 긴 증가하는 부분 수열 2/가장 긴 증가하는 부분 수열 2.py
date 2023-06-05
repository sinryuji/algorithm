n = int(input())
nums = list(map(int, input().split()))
s = [nums[0]]

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        if data[mid] >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer

for i in nums[1:]:
    if s[-1] < i:
        s.append(i)
    else:
        s[binary_search(i, s)] = i
        
print(len(s))