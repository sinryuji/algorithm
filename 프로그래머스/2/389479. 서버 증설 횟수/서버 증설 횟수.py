def solution(players, m, k):
    answer = 0
    
    server = []
    for p in players:
        for _ in range(p // m - len(server)):
            server.append(k)
            answer += 1
        server = [x - 1 for x in server if x - 1 > 0]
    
    return answer