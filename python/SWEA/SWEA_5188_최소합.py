# dfs 함수 구현
def dfs(x, y, resort):
    global result

    # 가지치기 조건
    if resort > result:
        return

    # 종료 조건
    if (x, y) == (N-1, N-1):
        if result > resort + arr[x][y]:
            result = resort + arr[x][y]
        return

    elif x >= N or y >= N:
        return

    dfs(x+1, y, resort + arr[x][y])
    dfs(x, y+1, resort + arr[x][y])

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in '_'*N]
    result = 250
    dfs(0, 0, 0)

    print(f'#{test_case} {result}')