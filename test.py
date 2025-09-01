def solution(n, times):
    answer = 0

    # 모든 사람이 심사 받는데 걸리는 최소 시간
    # 앞에 있는 사람은 비어있는 심사대
    # 또는 빨리 끝나는 심사대 기다렸다가 심사 받음
    st, ed = min(times), max(times) * n

    while st <= ed:
        mid = (st + ed) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people < n:
            st = mid + 1
        else:
            answer = mid
            ed = mid - 1

    return answer
