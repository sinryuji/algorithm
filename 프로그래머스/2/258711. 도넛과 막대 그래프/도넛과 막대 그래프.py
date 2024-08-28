def solution(edges):
    answer = [0, 0, 0, 0]
    
    d = {}
    for a, b in edges:
        if a not in d:
            d[a] = [0, 0]
        if b not in d:
            d[b] = [0, 0]
            
        d[a][0] += 1
        d[b][1] += 1
        
    for n, cnt in d.items():
        if cnt[0] > 1 and cnt[1] == 0:
            answer[0] = n
        elif cnt[0] == 0 and cnt[1] > 0:
            answer[2] += 1
        elif cnt[0] > 1 and cnt[1] > 1:
            answer[3] += 1
    
    answer[1] = d[answer[0]][0] - answer[2] - answer[3]
    
    return answer