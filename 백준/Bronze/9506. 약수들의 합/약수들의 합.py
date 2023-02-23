def isPerfect(n):
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        return divisor
    return None

while True:
    n = int(input())
    if n == -1:
        break
    divisor = isPerfect(n)
    if divisor == None:
        print(n, "is NOT perfect.")
    else:
        print(n, "=", end = " ")
        print(*divisor, sep = " + ")