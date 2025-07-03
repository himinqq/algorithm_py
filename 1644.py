n = int(input())

def get_primes(n): # 에라토스테네스의 체 (소수의 배수는 항상 소수가 아니다)
    is_prime = [True] * (n + 1) #1부터 n까지의 수
    is_prime[0] = is_prime[1] = False #0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1): # 2부터 √n까지 검사
        if is_prime[i]: # i가 소수이면
            for j in range(i * i, n + 1, i):
                is_prime[j] = False # i의 배수는 소수가 아님

    return [i for i in range(2, n + 1) if is_prime[i]] # 소수 리스트 반환

nums = get_primes(n)

ans = 0
start, end = 0,1

while end <= len(nums):
    tot = sum(nums[start:end])
    if tot <= n:
        if tot == n:
            ans += 1
        end += 1
    else:
        start += 1

print(ans)