import sys

input = sys.stdin.readline

N = int(input())
negative_nums = []
positive_nums = []
for _ in range(N):
    num = int(input())
    if num <= 0:
        negative_nums.append(num)
    else:
        positive_nums.append(num)

negative_nums.sort(reverse=True)
positive_nums.sort()

answer = 0
while len(negative_nums) > 1:
    answer += negative_nums.pop() * negative_nums.pop()
if negative_nums:
    answer += negative_nums.pop()

while len(positive_nums) > 1:
    num1, num2 = positive_nums.pop(), positive_nums.pop()
    if num1 * num2 > num1 + num2:
        answer += num1 * num2
    else:
        answer += num1 + num2
if positive_nums:
    answer += positive_nums.pop()

print(answer)