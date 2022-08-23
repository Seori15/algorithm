# 1. 각 순열마다 합을 구하는 함수 정의
def f(i, N):
    global minV
    global cnt
    cnt += 1
    if i == N:
        s = 0
        for k in range(N):
            s += arr[k][P[k]]
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

# 2. 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    P = [i for i in range(N)]
    minV = 1000
    cnt = 0
    f(0, N)
    print(f'#{test_case} {minV}')