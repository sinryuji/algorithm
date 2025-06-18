from itertools import combinations

def solution(n, q, ans):
    answer = 0
    lst = [i for i in range(1, n + 1)]
    m = len(ans)
    
    for c in combinations(lst, 5):
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                break
        else:
            answer += 1
                
    return answer