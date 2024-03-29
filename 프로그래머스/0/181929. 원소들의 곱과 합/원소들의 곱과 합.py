def solution(num_list):
    m = 1
    s = 0
    for num in num_list:
        m *= num
        s += num
    return 1 if m < s ** 2 else 0