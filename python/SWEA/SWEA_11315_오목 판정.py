di = [1, 1, 0, -1]
dj = [0, 1, 1, 1]

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[] for _ in '_'*N]
    for i in range(N):
        arr[i] = list(input())

    # 기본 result는 'NO'이다.
    # 2중 for문으로 2차원 배열을 돌면서 'o'를 찾는다.
    # 6/5/3/1시 각 4 방향으로 연속해서 'o'가 5개 있는지 찾는다.
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for dr in range(4):
                    n = 1
                    cnt = 1
                    while True:
                        ni, nj = i+(n*di[dr]), j+(n*dj[dr])
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                            n += 1
                            if cnt == 5:
                                result = 'YES'
                                break
                        else:
                            break

    print(f'#{test_case} {result}')
