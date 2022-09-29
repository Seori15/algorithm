# 입력값 설정하기
T = int(input())
for test_case in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())

# 값 변환을 위한 dict 생성
    dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

# arr 입력값을 숫자로 바꾼 nums 생성
    nums = []
    for i in arr:
        nums.append(dict[i])

# nums 버블 정렬
    for i in range(int(N) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# dict의 key와 value를 반전시킨 strings 생성
    strings = {v: k for k, v in dict.items()}

# nums를 다시 문자열로 바꾸어 출력
    result = []
    for i in nums:
        result.append(strings[i])

    print(tc)

    for i in result:
        print(i, end=' ')
    print()
