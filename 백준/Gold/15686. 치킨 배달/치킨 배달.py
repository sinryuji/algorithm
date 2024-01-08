def close(a,b): # 요구사항인 M개 만큼 치킨집을 폐업해보자
    global distance_min
    if a > len(chicken):
        return
    if b == M:
        distance_all = 0
        for r, c in house:
            distance = float('inf')
            for i in val:
                rr, cc = chicken[i]
                distance = min(distance, abs(rr-r)+abs(cc-c))
            distance_all += distance
        distance_min = min(distance_min, distance_all)
        return

    val.append(a)
    close(a+1, b+1)
    val.pop()
    close(a+1,b)

import sys
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken, house, val = [], [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

distance_min = float('inf')
close(0,0)
print(distance_min)
#출처: https://edder773.tistory.com/42 [개발하는 차리의 공부 일기:티스토리]