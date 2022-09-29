# dfs 함수 설정
def dfs(n):
    global ans

    # 종료 조건
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return

    # L개 중에서 2개를 뽑는 조합 경우의 수
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]

            # 가지치기 조건 추가. 바뀐 숫자가 이미 v에 있다면 방문하지 않는다.
            check = "".join(map(str, lst))
            if (n, check) not in v:
                dfs(n+1)
                v.append((n, check))

            lst[i], lst[j] = lst[j], lst[i]

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    st, N = input().split()
    N = int(N)
    lst = []
    for ch in st:
        lst.append(int(ch))
    L = len(lst)
    ans = 0  # 가능한 최소값
    v = []
    dfs(0)

    print(f'#{test_case} {ans}')