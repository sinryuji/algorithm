def solution(n, w, num):
    storage = [[] for _ in range(w)]
    
    idx = 0
    right = True
    for i in range(1, n + 1):
        storage[idx].append(i)
        if right:
            if idx == w - 1: right = False
            else: idx += 1
        else:
            if idx == 0: right = True
            else: idx -= 1
    
    n = len(storage)
    for i in range(n):
        m = len(storage[i])
        for j in range(m):
            if storage[i][j] == num:
                return m - j