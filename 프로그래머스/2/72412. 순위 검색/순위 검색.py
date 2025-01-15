from collections import defaultdict

def bs(arr, target):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        else:
            r = m
    return l

def solution(info, query):
    answer = []
    data = defaultdict(list)
    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
                        
    for k in data.keys():
        data[k].sort()
        
    for q in query:
        q = q.split()
        arr = data[(q[0], q[2], q[4], q[6])]
        s = int(q[7])
        answer.append(len(arr) - bs(arr, s))

    return answer