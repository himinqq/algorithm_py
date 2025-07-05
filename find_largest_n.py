def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 인덱스 저장

    for i in range(len(numbers)):
        # 스택 top 이 현재 값보다 작으면 조건만족 > 정답 저장
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)

    return answer
