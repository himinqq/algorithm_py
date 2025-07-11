def solution(numbers):
    # 숫자들을 문자열로 변환
    nums = list(map(str, numbers))

    # 정렬: 3을 곱해서 자릿수 보정 (ex: '3' → '333', '30' → '303030')
    nums.sort(key=lambda x: x * 3, reverse=True)

    # 결합
    answer = ''.join(nums)

    # '0000' 같은 경우 처리
    return '0' if answer[0] == '0' else answer
