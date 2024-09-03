def solution(seq, k):
    answer = []
    
    l, r = 0, 0
    length = len(seq)
    s = seq[0]
    
    while l <= r:
        if s <= k:
            if s == k:
                if len(answer) == 0:
                    answer = [l, r]
                else:
                    if r - l < answer[1] - answer[0]:
                        answer = [l, r]
            r += 1
            if r == length:
                break
            s += seq[r]
        else:
            s -= seq[l]
            l += 1
    
    return answer