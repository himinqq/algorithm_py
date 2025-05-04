
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# s의 값 가장 작게 만들기 위해 배열a 재배열. 단, 배열b 는 그대로 두어야 함
# b최대 * a최소 일 때 s최솟값

c = sorted(b,reverse=True)
a = sorted(a)
s = 0
for i in range(n):
    s += a[i] * c[i]
print(s)
# s의 최솟값 출력