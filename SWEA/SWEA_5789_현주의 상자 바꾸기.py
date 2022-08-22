# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0]*N

# L, R값 받아서 설정한 arr에 i값 넣어주기
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            arr[j] = i

    arr = map(str, arr)
    print(f'#{test_case} {" ".join(arr)}')