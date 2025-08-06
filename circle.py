import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):  # x축 기준 대칭만 계산
        # r2 범위 내 최대 y (y는 0 이상)
        max_y = math.floor((r2**2 - x**2)**0.5)
        # r1 범위 내 최소 y (y는 0 이상)
        min_y = math.ceil((r1**2 - x**2)**0.5) if x < r1 else 0
        answer += max(0, max_y - min_y + 1)
    return answer * 4  # 4사분면 대칭
