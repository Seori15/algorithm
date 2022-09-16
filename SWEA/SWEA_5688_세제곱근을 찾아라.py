# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # range(1, 10^6)에서 이분탐색
    start = 1
    end = 1000000
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if mid**3 == N:
            result = mid
            break
        elif start == end:
            break
        elif mid**3 < N:
            start = mid+1
        else:
            end = mid

    print(f'#{test_case} {result}')