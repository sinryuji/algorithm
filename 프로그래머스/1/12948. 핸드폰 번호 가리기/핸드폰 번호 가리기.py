def solution(phone_number):
    length = len(phone_number)
    return '*' * (length - 4) + phone_number[length - 4:]