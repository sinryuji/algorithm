def solution(absolutes, signs):
    return sum([n if signs[i] else -n for i, n in enumerate(absolutes)])