def solution(n, m, section):
    answer = 0
    
    pos = -100000
    for v in section:
        if v - pos >= m:
            pos = v
            answer += 1
        
    return answer