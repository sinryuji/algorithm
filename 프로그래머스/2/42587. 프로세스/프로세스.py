def solution(q, loc):
    answer = 1
    
    while q:
        x = q.pop(0)
        
        for n in q:
            if n > x:
                q.append(x)
                break
        else:
            if loc == 0:
                break
            answer += 1   

        loc = (loc - 1) % len(q)
        
    return answer