# DFS 풀이
def dfs(n, sm):
    global ans
    # 가지치기 조건
    if sm > ans:
        return

    # 종료 조건
    if n == N:
        if ans > sm:
            ans = sm
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, sm+arr[n][i])
            visited[i] = 0

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in '_'*N]
    ans = N*99
    visited = [0]*N
    dfs(0, 0)
    print(f'#{test_case} {ans}')