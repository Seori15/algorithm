# dfs 함수 설정
def dfs(start, n, battery):
    global result
    # 가지치기 조건
    if result < battery:
        return

    # 재귀 종료 조건
    if n == N - 1:
        if result > battery + arr[start][0]:
            result = battery + arr[start][0]
        return

    # 순열에 의해 남은 방 방문
    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, n + 1, battery + arr[start][i])
            visited[i] = 0


# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in '_' * N]
    result = 100 * N
    visited = [0] * N
    dfs(0, 0, 0)

    print(f'#{test_case} {result}')
