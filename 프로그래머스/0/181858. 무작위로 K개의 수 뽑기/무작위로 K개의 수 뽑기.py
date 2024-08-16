def solution(arr, k):
    answer = []
    
    i = 0
    while (i < len(arr) and len(answer) < k):
        if arr[i] not in answer:
            answer.append(arr[i])
        i += 1
    
    while (k > len(answer)):
        answer.append(-1)
    
    return answer