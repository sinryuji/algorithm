import sys
sys.setrecursionlimit(10**6)

def is_right(s):
    cnt = 0
    
    for c in s:
        if c == '(': 
            cnt += 1
        elif cnt < 1: 
            return False
        else: 
            cnt -= 1
        
    return True if cnt == 0 else False

def get_balanced_idx(w):
    left, right = 0, 0
    
    for i, c in enumerate(w):
        if c == '(': 
            left += 1
        else: 
            right += 1
        if left == right:
            return i+1
    
    return 0

def reverse(u):
    return ''.join([')' if c == '(' else '(' for c in u])
            
def recursion(w):
    if w == '':
        return w
    idx = get_balanced_idx(w)
    u, v = w[:idx], w[idx:]
    if is_right(u):
        return u + recursion(v)
    return '(' + recursion(v) + ')' + reverse(u[1:-1])

def solution(p):
    if is_right(p):
        return p
    return recursion(p)