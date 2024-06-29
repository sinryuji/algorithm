def solution(dartResult):
    answer = 0
    res = []
    dartResult = dartResult.replace('10', 't')
    
    score = 0
    for c in dartResult:
        if c.isdigit():
            score = int(c)
            continue
        elif c == 't':
            score = 10
            continue
        elif c == 'S':
            res.append(score)
        elif c == 'D':
            res.append(score ** 2)
        elif c == 'T':
            res.append(score ** 3)
        elif c == '*':
            res[-1] *= 2
            if len(res) > 1:
                res[-2] *= 2
        else:
            res[-1] *= -1
        score = 0
    
    return sum(res)