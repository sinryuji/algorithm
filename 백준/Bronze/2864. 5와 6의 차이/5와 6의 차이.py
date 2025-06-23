A, B = input().split()

min_ = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_ = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_, max_)