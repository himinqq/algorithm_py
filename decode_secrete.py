from itertools import combinations


def solution(n, q, ans):
    possible_code = list(combinations(range(1,n+1),5)) # 가능한 모든 정답 코드 조합 생성
    cnt = 0

    for code in possible_code:
        make_code = True
        for i in range(len(q)):
            if len(set(code) & set(q[i])) != ans[i]:
                make_code = False
                break
        if make_code:
            cnt += 1
    return cnt