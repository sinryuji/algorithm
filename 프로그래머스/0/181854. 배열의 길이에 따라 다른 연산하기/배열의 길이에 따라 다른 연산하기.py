def solution(arr, n):
    answer = []
    
    if len(arr) & 1:
        for i in range(len(arr)):
            if i & 1 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for i in range(len(arr)):
            if i & 1:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
                
    
    return answer