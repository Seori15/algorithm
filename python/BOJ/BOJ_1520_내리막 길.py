# [A] delta 방향 설정
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

# [B] dfs 함수 설정
def dfs(i, j):
    # 가지치기 조건. 이미 탐색한 적이 있다면 저장된 값을 반환
    if visited[i][j] != -1:
        return visited[i][j]

    # 종료 조건. M-1, N-1에 도달했을 때 1을 반환
    if (i, j) == (M-1, N-1):
        return 1;

    # visited 값에 Top-Down 형식으로 값을 저장한다.
    visited[i][j] = 0
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < M and 0 <= nj < N and arr[i][j] > arr[ni][nj]:
             visited[i][j] += dfs(ni, nj)

    return visited[i][j]

# [1] 입력값 설정
M, N = map(int, input().split())
arr = [[] for _ in '_'*M]
for i in range(M):
    arr[i] = list(map(int, input().split()))

visited = [[-1]*N for _ in '_'*M]
dfs(0, 0)

# for i in range(M):
#     print(visited[i])

print(visited[0][0])