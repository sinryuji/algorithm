def solution(storey):
    if storey < 10:
        return min(storey, 11 - storey)
    left = storey % 10
    return left + solution(storey // 10) if left < 5 or (left == 5 and (storey // 10) % 10 < 5) else 10 - left + solution(storey // 10 + 1)