# 중위순회 함수 설정
def inorder(n):
    if n:
        inorder(chL[n])
        print(par[n][1], end= '')
        inorder(chR[n])

# 입력값 설정
for test_case in range(1, 11):
    N = int(input())
    par = [[] for _ in '_'*(N+1)]
    chL = [0]*(N+1)
    chR = [0]*(N+1)

    for i in range(N):
        arr = list(input().split())
        par[i+1] = (int(arr[0]), arr[1])
        if len(arr) == 3:
            chL[i+1] = int(arr[2])
        elif len(arr) == 4:
            chL[i+1] = int(arr[2])
            chR[i+1] = int(arr[3])

    print(f'#{test_case}', end = ' ')
    inorder(1)
    print()