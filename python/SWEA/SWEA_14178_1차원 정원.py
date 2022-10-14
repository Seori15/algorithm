# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, D = map(int, input().split())

    # [2] 1개의 분무기는 reach만큼의 길이를 소화한다.
    reach = D*2 + 1
    result = N // reach
    if N%reach:
        result += 1
    print(f'#{test_case} {result}')
