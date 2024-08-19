def solution(strArr):
    d = dict()
    for str in strArr:
        d[len(str)] = d.get(len(str), 0) + 1
    
    return max(d.values())