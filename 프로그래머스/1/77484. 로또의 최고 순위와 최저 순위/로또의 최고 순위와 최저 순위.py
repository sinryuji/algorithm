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
    
    return [(6 if right_cnt == 0 and zero_cnt == 0 else 7) - zero_cnt - right_cnt, 6 if right_cnt == 0 else 7 - right_cnt]