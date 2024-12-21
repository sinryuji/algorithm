def timeToInt(time):
    return (int(time[:2]) * 60) + int(time[3:])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = timeToInt(video_len)
    pos = timeToInt(pos)
    op_start = timeToInt(op_start)
    op_end = timeToInt(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for cmd in commands:
        if cmd == 'next':
            pos += 10
        else:
            pos -= 10
        if op_start <= pos <= op_end:
            pos = op_end
        elif pos < 10:
            pos = 0
        elif pos > video_len - 10:
            pos = video_len
            
    minute = str(pos // 60)
    if len(minute) == 1:
        minute = '0' + minute
        
    second = str(pos % 60)
    if len(second) == 1:
        second = '0' + second
    
    return minute + ':' + second