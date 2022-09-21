# dfs 함수 설정
def dfs(n, sm):
    global ans

    # 가지치기 조건. 최소값을 찾는 문제라 시간이 오래 걸리기 때문에 설정.
    if ans <= sm:
        return

    # 종료조건
    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm+arr[n][j])
            visited[j] = 0  # 재귀 후 clearing 필수!!

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in '_'*N]

    ans = 10*N  # ans가 조건상 가능한 최대값.
    visited = [0]*N
    dfs(0, 0)

    print(f'#{test_case} {ans}')