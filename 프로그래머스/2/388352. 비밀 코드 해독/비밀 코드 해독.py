from itertools import combinations

def solution(n, q, ans):
    answer = 0
    m = len(ans)
    remove = list(filter(lambda i: ans[i] == 0, range(m)))
    
    lst = [i for i in range(1, n + 1)]
    for i in remove:
        lst = list(filter(lambda x: x not in q[i], lst))
    
    for c in combinations(lst, 5):
        for i in range(m):
            if len([j for j in q[i] if j in c]) != ans[i]:
                break
        else:
            answer += 1
                
    return answer
