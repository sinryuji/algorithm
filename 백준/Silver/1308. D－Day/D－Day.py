ty, tm, td = map(int, input().split())
dy, dm, dd = map(int, input().split())
def is_leap(year):
    result = False
    if year % 4 == 0:
        result = True
    if year % 100 == 0:
        result = False
    if year % 400 == 0:
        result = True
    return result

if dy > ty + 1000 or (dy == ty + 1000 and (dm > tm or (dm == tm and dd >= td))):
    print("gg")
else:
    answer = 0
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while ty != dy or tm != dm or td != dd:
        max_day = md[tm - 1]
        if tm == 2 and is_leap(ty):
            max_day += 1
        td += 1
        answer += 1
        if td > max_day:
            tm += 1
            td = 1
        if tm > 12:
            ty += 1
            tm = 1
    print(f"D-{answer}")