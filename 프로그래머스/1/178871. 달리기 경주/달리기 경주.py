def solution(players, callings):
    d = {}
    
    for i in range(len(players)):
        d[players[i]] = i
    
    for call in callings:
        idx = d[call]
        d[players[idx-1]] += 1
        d[call] -= 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    return players