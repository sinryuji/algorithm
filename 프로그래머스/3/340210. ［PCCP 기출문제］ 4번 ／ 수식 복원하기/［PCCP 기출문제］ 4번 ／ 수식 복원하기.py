def from_decimal(num: int, base: int) -> str:
    if num == 0:
        return '0'
    
    result = ''
    while num:
        result += str(num % base)
        num //= base
        
    return result[::-1]
        
    

def cal(num1: str, op: str, num2: str, base: int) -> str:
    num1 = int(num1, base)
    num2 = int(num2, base)
    
    if op == '+':
        res = num1 + num2
    else:
        res = num1 - num2
        
    return from_decimal(res, base)
    

def solution(expressions):
    answer = []
    
    m = 0
    erased, unerased = [], []
    for ex in expressions:
        sp = list(ex.split())
        m = max(max(m, int(sp[0][-1])), int(sp[2][-1]))
        if sp[-1] == 'X':
            erased.append(sp)
        else:
            unerased.append(sp)
            
    possible = [i for i in range(m + 1, 10)]
    
    for ex in unerased:
        tmp = []
        ans = ex[-1]
        for base in possible:
            tmp.append(cal(ex[0], ex[1], ex[2], base))
        remove = []
        for i in range(len(tmp)):
            if tmp[i] != ans:
                remove.append(possible[i])
        possible = [i for i in possible if i not in remove]
            
    for ex in erased:
        tmp = set()
        for base in possible:
            res = cal(ex[0], ex[1], ex[2], base)
            tmp.add(cal(ex[0], ex[1], ex[2], base))
        if len(tmp) > 1:
            ex[-1] = '?'
        else:
            ex[-1] = list(tmp)[0]
        answer.append(' '.join(ex))
        
    return answer