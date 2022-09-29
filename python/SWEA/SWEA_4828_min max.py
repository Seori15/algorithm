# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

# max값과 min값 구해서 차이값 출력하기
    M = num_list[0]
    m = num_list[0]
    for i in num_list:
        if i > M:
            M = i

        if i < m:
            m = i

    print(f'#{test_case} {M - m}')