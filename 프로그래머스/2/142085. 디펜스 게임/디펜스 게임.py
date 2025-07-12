import heapq

def solution(n, k, enemy):
    stage = len(enemy)
    if k >= stage:
        return stage
    q = []
    
    for i in range(stage):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            last = heapq.heappop(q)
            if last > n:
                return i
            n -= last
    
    return stage