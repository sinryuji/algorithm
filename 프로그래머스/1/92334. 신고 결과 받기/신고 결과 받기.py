def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = dict()
    index = dict()
    cnt = dict()
    
    for idx, id in enumerate(id_list):
        reported[id] = []
        index[id] = idx
        cnt[id] = 0

    for r in set(report):
        a, b = r.split()
        reported[b].append(a)
        
    for id in id_list:
        if len(reported[id]) >= k:
            for id in reported[id]:
                answer[index[id]] += 1
        
    return answer