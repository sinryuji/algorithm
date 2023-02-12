def printSquare(n):
    if n == 1:
        return ['*']

    square = printSquare(n // 3)
    arr = []

    for i in square:
        arr.append(i * 3)
    for i in square:
        arr.append(i + ' ' * (n // 3) + i)
    for i in square:
        arr.append(i * 3)

    return arr
    
n = int(input())
print('\n'.join(printSquare(n)))