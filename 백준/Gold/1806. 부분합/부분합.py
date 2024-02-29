import sys
input = sys.stdin.readline

def solution():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    left, right = 0, 0
    answer, sum_ = N, 0
    flag = False

    for left in range(N):
        while sum_ < S and right < N:
            sum_ += nums[right]
            right += 1
        if sum_ >= S:
            flag = True
            answer = min(answer, right - left)
        sum_ -= nums[left]

    if not flag:
        print(0)
    else:
        print(answer)

if __name__ == '__main__':
    solution()
