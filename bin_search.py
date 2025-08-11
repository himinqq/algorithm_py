from bisect import bisect_right, bisect_left

N = int(input())
a = list(map(int, input().split()))

table = {}
nums = set(a)
sorted = sorted(nums) # a 배열 중복 제거 후 정렬

for i, num in enumerate(sorted):
    table[num] = i # 정렬 순서대로 작은 수 부터 번호 부여

a = [table[num] for num in a] # 원래 순서대로 출력
print(*a)