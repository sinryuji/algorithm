def solution(N, stages):
    arr = []
    for i in range(1, N+1):
        challenge = 0
        over = 0
        for j in stages:
            if j == i:
                challenge += 1
            if j >= i:
                over += 1
        arr.append((challenge / over if over > 0 else 0, i))
    arr.sort(key=lambda x: (-x[0]))
    
    return [i[1] for i in arr]
        