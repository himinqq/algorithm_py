from bisect import bisect_right


def solution(A, B):
    answer = 0
    B.sort()
    used = [False] * len(B)

    for a in A:
        idx = bisect_right(B,a)
        while idx < len(B) and used[idx]:
            idx += 1
        if idx < len(B):
            answer += 1
            used[idx] = True
    # B팀원이 얻을 수 있는 최대 승점
    # A > B 로 B 배열 조작할 때 얻을 수 있는 최댓값
    return answer
