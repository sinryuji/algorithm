from collections import Counter

def solution(points, routes):
    answer = 0
    
    path = []
    for route in routes:
        sec = 0
        for i in range(len(route) - 1):
            cur_r, cur_c = points[route[i]-1]
            nxt_r, nxt_c = points[route[i+1]-1]
            
            while cur_r != nxt_r:
                path.append((sec, cur_r, cur_c))                
                if cur_r < nxt_r:
                    cur_r += 1
                else:
                    cur_r -= 1
                sec += 1

            while cur_c != nxt_c:
                path.append((sec, cur_r, cur_c))                
                if cur_c < nxt_c:
                    cur_c += 1
                else:
                    cur_c -= 1
                sec += 1
        path.append((sec, cur_r, cur_c))
    
    counter = Counter(path)
    for count in counter.items():
        if count[1] > 1:
            answer += 1
    
    return answer