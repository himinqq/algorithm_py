import math


def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        y = math.sqrt(d ** 2 - x ** 2)  # 원의 방정식을 사용해서 y 구함 ( x² + y² ≤ d² )

        # 문제에서 주어진 조건: (k의 배수, k의 배수)인 격자점만 확인
        answer += y // k + 1 # y보다 작거나 같은 k의 배수가 몇 개 있는지 계산 (원점 포함 + 1)

    return answer