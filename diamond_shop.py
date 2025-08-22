# 특정 범위 구매해되, 모든 종류의 보석 적어도 1개 이상 포함하는 가장 짧은 구간
def solution(gems):
    n = len(gems)
    answer = [0, n - 1]  # 최댓값으로 초기화
    start, end = 0, 0
    kind = len(set(gems))

    counter = {gems[0]: 1}  # 현재 구간 보석 개수

    while start < n and end < n:
        # 보석 종류와 같아질때까지 end 를 증가시키기
        if len(counter) < kind:
            end += 1
            if end == n:
                break
            counter[gems[end]] = counter.get(gems[end], 0) + 1

        if len(counter) == kind:
            # 정답 후보에 기록
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            # start 증가시켜서 최소 범위 찾기
            counter[gems[start]] -= 1
            if counter[gems[start]] == 0:
                del counter[gems[start]]
            start += 1

    return [answer[0] + 1, answer[1] + 1]


