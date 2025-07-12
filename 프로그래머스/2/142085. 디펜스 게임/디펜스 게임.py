import heapq

def solution(n, k, enemy):
    q = enemy[:k]
    heapq.heapify(q)
    for i in range(k, len(enemy)):
        n -= heapq.heappushpop(q, enemy[i])
        if n < 0:
            return i
    return len(enemy)