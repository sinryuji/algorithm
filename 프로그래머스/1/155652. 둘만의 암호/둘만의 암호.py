def solution(s, skip, index):
    answer = ''
    
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    for c in s:
        cur = alpha.index(c)
        answer += alpha[(cur + index) % len(alpha)]
    
    return answer