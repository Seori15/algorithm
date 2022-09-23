# DFS 풀이
# dfs 함수 설정
def dfs(n, s):
    global result
    # 종료 조건
    if n == L:
        if B <= s < result:
            result = s
        return

    dfs(n+1, s+height[n]) # 더하거나
    dfs(n+1, s)           # 더하지 않거나

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    L = len(height)
    result = 10000*N
    dfs(0, 0)
    print(f'#{test_case} {result - B}')

# 부분집합 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort()

    # 각 부분집합에서 0 이상의 min_gap 값을 저장한다.
    L = len(height)
    min_gap = 10000*N
    for i in range(2**L):
        gap = -B
        for j in range(L):
            if i & (1 << j):
                gap += height[j]
        if 0 <= gap < min_gap:
            min_gap = gap

    print(f'#{test_case} {min_gap}')