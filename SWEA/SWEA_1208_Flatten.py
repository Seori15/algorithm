# 입력값 받기
for test_case in range(1, 11):
    N = int(input())
    num_list = list(map(int, input().split()))

# 평탄화 작업 N회. list의 Max값 min값에 각각 -1 +1
    for i in range(N):
        M = 0
        m = 100
        for j in range(100):
            if M < num_list[j]:
                M = num_list[j]
                Mi = j
            if m > num_list[j]:
                m = num_list[j]
                mi = j
        num_list[Mi] += -1
        num_list[mi] += 1

# 평탄화 작업 이후 Max, min값 찾아서 출력하기
    M = 0
    m = 100
    for i in num_list:
        if M < i:
            M = i
        if m > i:
            m = i

    print(f'#{test_case} {M - m}')