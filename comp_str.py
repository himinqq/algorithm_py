def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) + 1): # 문자열 몇 개씩 자를지 정하기
        res = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i): # 반복되는 패턴 개수 세기

            if tmp == s[j:i + j]: # 현재 tmp와 같은 문자열이면 cnt만 증가
                cnt += 1
            else: # 같지 않으면 지금까지의 압축 문자열을 res에 더함
                if cnt != 1:
                    res = res + str(cnt) + tmp
                else:
                    res = res + tmp

                tmp = s[j:j + i] # # 새로운 비교 문자열로 갱신
                cnt = 1 # 카운터 초기화

        result.append(len(res)) #압축된 문자열의 길이

    return min(result)
