from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

# + - x / 순서대로
op_cnt = list(map(int, input().split()))
op = ["+", "-", "x", "/"]
operator = []

for i in range(len(op_cnt)):
    for cnt in range(op_cnt[i]):
        operator.append(op[i])


def calculate(numbers, ops):
    idx = 0
    total = numbers[0]
    for i in range(1, len(numbers)):
        if ops[idx] == '+':
            total += numbers[i]
        elif ops[idx] == '-':
            total -= numbers[i]
        elif ops[idx] == 'x':
            total *= numbers[i]
        elif ops[idx] == '/':
            #total //= numbers[i] 파이썬 스타일 나눗셈
            total = int(total / numbers[i])
        if idx < len(numbers) - 2:
            idx += 1
    return total

min_res  = 10**18
max_res = -10**18 #연산 결과 음수 일 수 있으니까 0으로 설정하면 안됨
for comb in permutations(operator, r=len(numbers) - 1):
    res = calculate(numbers, comb)
    min_res = min(min_res,res)
    max_res = max(max_res,res)

print(max_res,min_res,end="\n")