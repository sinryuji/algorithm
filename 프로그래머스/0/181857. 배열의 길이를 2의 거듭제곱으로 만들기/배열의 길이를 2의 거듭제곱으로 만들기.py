def solution(arr):
    i = 0
    while 2 ** i < len(arr):
        i += 1
    n = 2 ** i
    
    arr += [0] * (n - len(arr))
    
    return arr