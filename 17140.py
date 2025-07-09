from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def r_operation(A):
    new_A = []
    max_len = 0

    for row in A: # 행마다 연산 적용
        counter = Counter(row)
        if 0 in counter:
            del counter[0]
        sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for num, cnt in sorted_items:
            new_row.extend([num, cnt])

        max_len = max(max_len, len(new_row))
        new_A.append(new_row)

    # 0으로 채우기 (길이 맞추기, 최대 100)
    for row in new_A:
        row += [0] * (max_len - len(row))
        if len(row) > 100:
            del row[100:]

    return new_A

def c_operation(A):
    transposed = list(zip(*A))
    operated = r_operation(transposed)
    return list(zip(*operated))

time = 0
while time <= 100:
    if r - 1 < len(arr) and c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        print(time)
        break

    row = len(arr)
    col = len(arr[0])

    if row >= col:
        arr = r_operation(arr)
    else:
        arr = c_operation(arr)

    time += 1
else:
    print(-1)
