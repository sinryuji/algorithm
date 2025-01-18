def solution(record):
    answer = []
    
    d = dict()
    for data in record:
        data = list(data.split())
        if data[0] == 'Enter' or data[0] == 'Change':
            d[data[1]] = data[2]
    
    for data in record:
        data = list(data.split())
        if data[0] == 'Enter':
            answer.append(d[data[1]] + '님이 들어왔습니다.')
        elif data[0] == 'Leave':
            answer.append(d[data[1]] + '님이 나갔습니다.')
    
    return answer