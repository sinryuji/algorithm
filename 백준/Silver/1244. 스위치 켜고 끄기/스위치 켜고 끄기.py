n = int(input())
switch = list(map(int, input().split())) # 스위치 상태 저장할 리스트
change = {1: 0, 0: 1} # 스위치 바꾸는 dictionary

for _ in range(int(input())):
    gender, no = map(int, input().split())
    i = 1
    # 남자일 때
    if gender == 1:
        while no * i - 1 < n:
            switch[no*i-1] = change[switch[no*i-1]]
            i += 1
    # 여자일 때
    elif gender == 2:
        switch[no-1] = change[switch[no-1]]
        while 1 <= no-i and no+i < n+1 and switch[no-i-1] == switch[no-1+i]:
            switch[no-1-i] = change[switch[no-1-i]]
            switch[no-1+i] = change[switch[no-1+i]]
            i += 1

# 출력
for i in range(n):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()