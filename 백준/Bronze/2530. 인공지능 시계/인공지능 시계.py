import datetime

a, b, c = map(int, input().split())
d = int(input())
now = datetime.datetime(2023, 6, 10, a, b, c) + datetime.timedelta(seconds=d)
print(now.hour, now.minute, now.second)