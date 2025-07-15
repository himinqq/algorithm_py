def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num: #이전 값보다 현재값이 더 크면
            stack.pop() # 현재 값보다 작은 이전값 모두 제거
            k -= 1
        stack.append(num)

    if k > 0: # 모두 지웠는데 k 남아있으면211
        stack = stack[:-k] #끝에서 k개 제거

    return ''.join(stack)
