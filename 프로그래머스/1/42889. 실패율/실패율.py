def solution(N, stages):
    arr = []
    cnt = [0] * (N + 2)
    for stage in stages:
        cnt[stage] += 1
    
    for i in range(1, N + 1):
        over = sum(cnt[i:])
        challenge = cnt[i]
        arr.append((i, 0 if over == 0 else challenge / over))
    
    return list(i[0] for i in sorted(arr, key=lambda x: -x[1]))