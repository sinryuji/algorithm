def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    cnt = 0
    for _ in range(n):
        planets.append(list(map(int, input().split())))
    for planet in planets:
        start_dis = get_distance(x1, y1, planet[0], planet[1])
        end_dis = get_distance(x2, y2, planet[0], planet[1])
        if (start_dis < planet[2] and end_dis > planet[2]) or \
            (start_dis > planet[2] and end_dis < planet[2]):
            cnt+= 1
    print(cnt)