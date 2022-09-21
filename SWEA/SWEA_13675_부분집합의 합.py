# DFS 함수 설정
def dfs(n, sm, cnt):
    global ans

    if sm > K:  # 가지치기를 사용해도 좋으나 경우에 따라 시간이 늘어남
        return

    if n == N: # 종료 조건
        if sm == K and cnt == CNT:
            ans += 1
        return

    # 사용하는 경우
    dfs(n+1, sm+lst[n], cnt+1)
    # 사용하지 않는 경우
    dfs(n+1, sm, cnt)

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    N = len(lst)

    ans = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {ans}')