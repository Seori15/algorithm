# 비트 연산 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = float(input())

    # 2^12승 곱해서 float와 int가 같으면 표현 가능.
    result = ''
    num = N*(2**12)
    if int(num) == num:
        for i in range(11, -1, -1):
            if int(num) & (1<<i):
                result += '1'
            else:
                result += '0'

        # 뒤에 0 쳐내고 출력
        result = result.rstrip('0')

    # 같지 않다면 표현 불가능
    else:
        result = 'overflow'
    print(f'#{test_case} {result}')