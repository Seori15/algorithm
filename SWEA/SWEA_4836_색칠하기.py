# 입력값 설정하기
T = int(input())
for test_case in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    result = 0

    N = int(input())
    for i in range(N):
        a, b, c, d, e = map(int, input().split())

# 2차원 범위 내 주어진 범위에 e만큼 값 더하기
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                arr[x][y] += e

# 값이 3인 칸 수 찾기
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 3:
                result += 1

    print(f'#{test_case} {result}')
