def solution(n, info):
    answer = []
    max_diff = 0
    
    def cal_diff(shoot):
        peach_score, ryan_score = 0, 0
        for i in range(11):
            if info[i] == 0 and shoot[i] == 0:
                continue
            if info[i] >= shoot[i]:
                peach_score += (10 - i)
            else:
                ryan_score += (10 - i)
        return ryan_score - peach_score
    
    def dfs(shoot, n, i):
        nonlocal answer, max_diff
        if i == 11:
            if n != 0:
                shoot[10] = n
        
            score_diff = cal_diff(shoot)
            if score_diff <= 0:
                return

            result = shoot[::]
            if score_diff > max_diff:
                max_diff = score_diff
                answer = [result]
                return

            if score_diff == max_diff:
                answer.append(result)
            return
    
        if info[i] < n:
            shoot.append(info[i] + 1)
            dfs(shoot, n - info[i] - 1, i + 1)
            shoot.pop()
            
        shoot.append(0)
        dfs(shoot, n, i + 1)
        shoot.pop()
        
    dfs([], n, 0)
    
    if len(answer) == 0:
        return [-1]
    
    answer.sort(key=lambda x: x[::-1], reverse=True)
    
    return answer[0]