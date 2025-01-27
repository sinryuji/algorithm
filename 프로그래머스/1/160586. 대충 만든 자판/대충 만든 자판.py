def solution(keymap, targets):
    answer = []
    
    d = dict()
    for key in keymap:
        for i, c in enumerate(key):
            if c in d:
                d[c] = min(d[c], i + 1)
            else:
                d[c] = i + 1
                
    for target in targets:
        tmp = 0
        for c in target:
            if c in d:
                tmp += d[c]
            else:
                tmp = -1
                break
        answer.append(tmp)
    
    return answer