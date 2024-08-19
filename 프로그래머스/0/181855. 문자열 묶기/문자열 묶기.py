def solution(strArr):
    d = dict()
    for str in strArr:
        if len(str) in d:
            d[len(str)] += 1
        else:
            d[len(str)] = 1
    
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][1]