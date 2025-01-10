import math

def time_to_minute(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(fees, records):
    answer = []
    cars = dict()
    
    for record in records:
        time, car_num, act = record.split()
        time = time_to_minute(time)
        if act == 'IN':
            if car_num not in cars:
                cars[car_num] = [time, 0, 'IN']
            else:
                cars[car_num][0] = time
                cars[car_num][2] = 'IN'
        else:
            cars[car_num][2] = 'OUT'
            cars[car_num][1] += time - cars[car_num][0]
            cars[car_num][0] = time
            
    cars = sorted(list(cars.items()))
    midnight = time_to_minute('23:59')
    for car_num, state in cars:
        if state[2] == 'IN':
            state[1] += midnight - state[0]
        charge = 0
        print(state[1])
        if state[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((state[1] - fees[0]) / fees[2]) * fees[3])
    
    return answer