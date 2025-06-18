from itertools import combinations

def solution(n, qs, ans):
    combi = list(combinations(range(1, n + 1), 5))
    
    for q, cnt in zip(qs, ans):
        combi = [c for c in combi if len(set(c) & set(q)) == cnt]
    
    return len(combi)