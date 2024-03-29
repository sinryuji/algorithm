def solution(a, d, included):
    answer = 0
    for i, b in enumerate(included):
        if b:
            answer += a + (d * i)
    return answer