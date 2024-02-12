import sys
input = sys.stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = max(nums) + 1
    l = [False] * (max_num)
    ans = [0] * (max_num)
    
    for num in nums:
        l[num] = True
    
    for num in nums:
        for target in range(num*2, max_num, num):
            if l[target]:
                ans[num] += 1
                ans[target] -= 1
    
    ans_str = ''
    for num in nums:
        ans_str += str(ans[num]) + ' '
    print(ans_str)

main()