# 1. 함수 설정
def f(i, j, N):
    stack = [(i, j)]
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    # stack이 빌 때까지 상하좌우를 탐색하면서, 이동 가능한 좌표를 stack에 추가한다.
    # stack을 pop해가면서 maze[i][j]가 3인 좌표를 찾는다.
    while stack:
        i, j = stack.pop()
        if maze[i][j] == 3:
            return 1

        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append([ni, nj])
                visited[ni][nj] = 1

    # stack이 비는 동안 maze[i][j]가 3인 좌표가 없었다면 0을 반환한다.
    return 0

# 2. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                i, j = x, y
                break

# 3. 형식에 맞게 출력하기
    result = f(i, j, N)
    print(f'#{test_case} {result}')
