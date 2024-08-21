def strToDay(str):
    y, m, d = map(int, str.split('.'))
    return (y * 12 * 28) + ((m - 1) * 28) + d

def solution(today, terms, privacies):
    answer = []
    t = strToDay(today)
    d = {}
    for term in terms:
        a, b = term.split()
        d[a] = int(b)
        
    for i, p in enumerate(privacies):
        day, term = p.split()
        if strToDay(day) + d[term] * 28 <= t:
            answer.append(i+1)
    
    return answer