def solution(seq, k):
    answer = []
    
    l, r = 0, 0
    length = len(seq)
    s = seq[0]
    
    while l <= r:
        if s <= k:
            if s == k:
                answer.append((l, r))
            r += 1
            if r == length:
                break
            s += seq[r]
        else:
            s -= seq[l]
            l += 1
    
    answer.sort(key = lambda x: (x[1] - x[0], x[0]))
    
    return answer[0]