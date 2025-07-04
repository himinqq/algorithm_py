# n을 k진수로 바꾸기
# 조건 만족하는 소수 찾기
import math


def convert(n, k):
    temp = "0123456789ABCDEF"
    q, r = divmod(n, k)
    if q == 0:
        return temp[r]
    return convert(q, k) + temp[r]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    conv_n = convert(n, k)
    p_count = 0

    candidate_p = list(map(int,filter(lambda x: x!= '',conv_n.split('0'))))

    for i in range(len(candidate_p)):
        if is_prime(candidate_p[i]):
            p_count += 1

    return p_count
