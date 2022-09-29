# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    arr = [input() for i in range(5)]

# 15x5 범위에서, 값을 result에 순서대로 추가한다.
    result = ''
    for j in range(15):
        for i in range(5):
            try:
                result += arr[i][j]
            except IndexError:
                continue
    print(f'#{test_case} {result}')