from itertools import permutations

def calculate(a, op, b):
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # '*'
        return a * b

def solution(expression):
    ops = ['+', '-', '*']
    used_ops = [op for op in ops if op in expression]

    # 수식 파싱
    exp = []
    tmp = ""
    for ch in expression:
        if ch in ops:
            exp.append(tmp)
            exp.append(ch)
            tmp = ""
        else:
            tmp += ch
    exp.append(tmp)

    max_result = 0

    for priority in permutations(used_ops):
        exp_copy = exp[:] # 원본 복사
        for op in priority: # 우선순위 높은 연산자부터 계산
            stack = []
            i = 0
            while i < len(exp_copy):
                if exp_copy[i] == op: # 현재 우선순위 연산자 나오면 계산
                    a = stack.pop() # 연산자 앞
                    b = exp_copy[i+1] # 연산자 뒤
                    res = str(calculate(a, op, b)) # 계산
                    stack.append(res)
                    i += 2  # 현재 연산자 + 다음 피연산자까지 스킵
                else: # 아니면 스택에 저장
                    stack.append(exp_copy[i])
                    i += 1
            exp_copy = stack  # 이번 우선순위로 처리된 결과
        max_result = max(max_result, abs(int(exp_copy[0])))

    return max_result
