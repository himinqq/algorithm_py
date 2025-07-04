def solution(n, t, m, p):
    answer = ''
    test = ''
    for i in range(t * m):
        test += str(convert(i, n))
    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer


# 10진수 -> n진수
def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
