import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    
    num = ''
    while n > 0:
        num += str(n % k)
        n //= k
    num = num[::-1]
    split_num = num.split('0')
    
    for x in split_num:
        if not x:
            continue
        answer += is_prime(int(x))
    
    return answer