def solution(genres, plays):
    answer = []
    
    d = dict()
    for i in range(len(genres)):
        d.setdefault(genres[i], []).append((i, plays[i]))
        
    for k in d.keys():
        d[k].sort(key=lambda x: (x[1], -x[0]))
        
    sorted_keys = sorted(d.keys(), key=lambda k: sum(v[1] for v in d[k]), reverse=True)
    
    for k in sorted_keys:
        for _ in range(2):
            if d[k]:
                i, v = d[k].pop()
                answer.append(i)
    
    return answer