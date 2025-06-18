def solution(s):
    answer = []
    d = {}
    
    for i, c in enumerate(s):
        if c in d:
            answer.append(i - d[c])
        else:
            answer.append(-1)
        d[c] = i
    
    return answer