N = input()
l = len(N)
answer = 0

for i in range(1, l):
    answer += 9 * i * (10 ** (i - 1))
answer += l * (int(N)- (10 ** (l - 1)) + 1)

print(answer)