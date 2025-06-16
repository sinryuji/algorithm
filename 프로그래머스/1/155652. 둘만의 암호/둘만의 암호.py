import string

def solution(s, skip, index):
    answer = ''
    
    alpha = set(string.ascii_lowercase)
    alpha -= set(skip)
    alpha = sorted(alpha)
    dic = {c:idx for idx, c in enumerate(alpha)}
    
    l = len(alpha)
    for c in s:
        answer += alpha[(dic[c] + index) % l]
    
    return answer