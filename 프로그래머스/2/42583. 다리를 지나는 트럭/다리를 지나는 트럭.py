from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    s = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    while truck_weights :
        w = bridge.popleft()
        s -= w
        nxt = truck_weights.popleft()
        if s + nxt <= weight:
            bridge.append(nxt)
            s += nxt
        else:
            truck_weights.appendleft(nxt)
            bridge.append(0)
        answer += 1
        
    answer += bridge_length
    
    return answer