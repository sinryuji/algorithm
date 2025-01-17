def solution(relation):
    answer = []
    row, col = len(relation), len(relation[0])
    
    for i in range(1, 1 << col):
        s = set()
        for j in range(row):
            tmp = ''
            for k in range(col):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            s.add(tmp)
            
        if len(s) == row:
            put = True
            for n in answer:
                if (n & i) == n:
                    put = False
                    break
            if put:
                answer.append(i)
    print(answer)
    return len(answer)