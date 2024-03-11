N = int(input())


def solve():
    sieve = [False, False] + [True] * (N - 1)
    primes = []

    for i in range(2, N + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * 2, N + 1, i):
                sieve[j] = False
                
    right = 0
    answer, sum_ = 0, 0
    primes_len = len(primes)
    
    for left in range(primes_len):
        while sum_ < N and right < primes_len:
            sum_ += primes[right]
            right += 1
        if sum_ == N:
            answer += 1
        sum_ -= primes[left]
        
    print(answer)

solve()