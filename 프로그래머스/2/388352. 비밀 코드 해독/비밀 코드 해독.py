from itertools import combinations

def solution(n, qs, ans):
    remove_idx = [i for i, val in enumerate(ans) if val == 0]
    remove = set().union(*(qs[idx] for idx in remove_idx))
    
    lst = [x for x in range(1, n + 1) if x not in remove]
    combi = list(combinations(lst, 5))
    
    for q, cnt in zip(qs, ans):
        combi = [c for c in combi if len(set(c) & set(q)) == cnt]
    
    return len(combi)