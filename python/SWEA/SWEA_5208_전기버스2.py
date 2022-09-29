# 재귀함수 설정
def f(n, remain, exchange):
    global ans
    # 가지치기 조건
    if exchange > ans:
        return

    # 종료 조건
    if n == N:
        if ans > exchange:
            ans = exchange
        return

    # 배터리 잔량이 0이라면 교체해야한다. 0이 아니면 교체는 선택이다.
    if remain == 0:
        f(n+1, battery[n-1]-1, exchange + 1)
    else:
        f(n+1, remain-1, exchange)           # 배터리 교체X
        f(n+1, battery[n-1]-1, exchange + 1) # 배터리 교체

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, *battery = list(map(int, input().split()))
    ans = N
    f(2, battery[0]-1, 0)
    print(f'#{test_case} {ans}')