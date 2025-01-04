def solution(lottos, win_nums):
    zero_cnt = 0
    right_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        else:
            for n in win_nums:
                if lotto == n:
                    right_cnt += 1
                    break
    
    rate = [6, 6, 5, 4, 3, 2, 1]
    
    return [rate[zero_cnt + right_cnt], rate[right_cnt]]