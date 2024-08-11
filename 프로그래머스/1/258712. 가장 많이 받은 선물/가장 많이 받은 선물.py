def solution(friends, gifts):
    answer = 0
    n = len(friends)
    record = [[0] * n for _ in range(n)]
    score = [0] * n
    d = dict()
    for i in range(len(friends)):
        d[friends[i]] = i
    
    for gift in gifts:
        a, b = gift.split()
        record[d[a]][d[b]] += 1
        score[d[a]] += 1
        score[d[b]] -= 1
        
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                if record[i][j] > record[j][i]:
                    cnt += 1
                elif ((record[i][j] == 0 and record[j][i] == 0) or record[i][j] == record[j][i]) and score[i] > score[j]:
                    cnt += 1
        answer = max(answer, cnt)
    
    return answer