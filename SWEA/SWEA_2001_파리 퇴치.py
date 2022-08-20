# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열에서 MxM 크기의 블럭으로 탐색하기
    result = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            Paris = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    Paris += arr[i][j]
            if result < Paris:
                result = Paris

    print(f'#{test_case} {result}')
