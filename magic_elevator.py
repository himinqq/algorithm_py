def solution(storey):
    answer = 0
    while storey > 0:
        remainder = storey % 10
        next_digit = (storey // 10) % 10

        if remainder > 5 or (remainder == 5 and next_digit >= 5):
            answer += 10 - remainder
            storey += 10 - remainder  # 올림 처리
        else:
            answer += remainder
        storey //= 10
    return answer
