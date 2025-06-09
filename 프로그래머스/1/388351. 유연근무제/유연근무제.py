from collections import deque
import itertools

def solution(schedules, timelogs, startday):
    answer = 0
    
    for log, sche in zip(timelogs, schedules):
        log = deque(log)
        log.rotate(startday - 1)
        
        succeed = True
        sche = (sche // 100 * 60) + sche % 100
        for time in itertools.islice(log, 5):
            time = (time // 100 * 60) + time % 100
            if time - sche > 10:
                succeed = False
                break
                
        if succeed:
            answer += 1
            
    return answer