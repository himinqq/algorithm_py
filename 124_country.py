def solution(n):
    result = []
    while n:
        remain = n % 3
        if not remain: #나머지가 0이면 (3의 배수)
            remain = 4 # 0 대신 4를 사용
            n -= 1 # 윗자리에서 빌려오기
        result.append((str(remain)))
        n //= 3 # 다음 자리 확인
    return ''.join(result[::-1])