def solution(survey, choices):
    answer = ''
    
    d = {
        'RT': [0, 3, 2, 1, 0, -1, -2, -3],
        'TR': [0, -3, -2, -1, 0, 1, 2, 3],
        'CF': [0, 3, 2, 1, 0, -1, -2, -3],
        'FC': [0, -3, -2, -1, 0, 1, 2, 3],
        'JM': [0, 3, 2, 1, 0, -1, -2, -3],
        'MJ': [0, -3, -2, -1, 0, 1, 2, 3],
        'AN': [0, 3, 2, 1, 0, -1, -2, -3],
        'NA': [0, -3, -2, -1, 0, 1, 2, 3],
    }
    
    rt = cf = jm = an = 0
    for idx, sur in enumerate(survey):
        if sur == 'RT' or sur == 'TR':
            rt += d[sur][choices[idx]]
        elif sur == 'CF' or sur == 'FC':
            cf += d[sur][choices[idx]]
        elif sur == 'JM' or sur == 'MJ':
            jm += d[sur][choices[idx]]
        else:
            an += d[sur][choices[idx]]
            
    if rt >= 0:
        answer += 'R'
    else:
        answer += 'T'
    if cf >= 0:
        answer += 'C'
    else:
        answer += 'F'
    if jm >= 0:
        answer += 'J'
    else:
        answer += 'M'
    if an >= 0:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer