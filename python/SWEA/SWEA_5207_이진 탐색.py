# dfs 함수 설정
def dfs(n, start, end, left):
    global ans
    # 중간 종료 조건. n이 탐색 범위를 벗어나면 return
    if n < A[start] or n > A[end] or start > end:
        return

    mid = (start + end) // 2
    # 종료 조건. mid에서 n을 찾았을 때, ans + 1
    if A[mid] == n:
        ans += 1
        return

    # 이전에 left를 탐색했다면 다음엔 반대쪽을 탐색하도록 설계
    if left:
        dfs(n, start, mid-1, 1-left)
    else:
        dfs(n, mid+1, end, 1-left)



# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = tuple(map(int, input().split()))

    # left / right 중 어디에 있는지 파악해서 재귀
    ans = 0
    for b in B:
        if b < A[(N-1)//2]:
            dfs(b, 0, N-1, 1)
        else:
            dfs(b, 0, N-1, 0)
    print(f'#{test_case} {ans}')