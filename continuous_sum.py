def solution(sequence, k):
    n = len(sequence)
    start = 0
    end = 0
    total = sequence[0]
    result = []
    min_len = float('inf')

    while start <= end and end < n:
        if total == k:
            if end - start + 1 < min_len: #현재 구간 길이가 더 짧으면
                min_len = end - start + 1
                result = [start, end] #정답 갱신
            total -= sequence[start] #다음 구간 확인
            start += 1

        elif total < k:
            end += 1
            if end < n:
                total += sequence[end]

        else: # total > k
            total -= sequence[start]
            start += 1

    return result
