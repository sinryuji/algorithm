import math

def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    
    num = ''
    zero = ord('0')
    while n > 0:
        num += chr(n % k + zero)
        n //= k
    num = num[::-1]
    
    tmp = ''
    zero_flag = True
    for c in num:
        if c == '0':
            zero_flag = False
            if tmp:
                answer += is_prime(tmp)
            tmp = ''
        else:
            tmp += c
            
    if zero_flag:
        answer += is_prime(num)
    elif tmp:
        answer += is_prime(tmp)
    
    return answer