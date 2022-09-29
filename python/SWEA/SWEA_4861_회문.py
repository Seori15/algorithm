# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

# 회문인 경우 cnt가 증가하며, cnt가 M이면 result를 출력한다.
    result = ''
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):

# X방향 회문체크
            if arr[i][j] == arr[i][j+M-1]:
                result = ''
                cnt = 0
                for k in range(M):
                    if arr[i][j+k] == arr[i][j+M-1-k]:
                        result += arr[i][j+k]
                        cnt += 1
                if cnt == M:
                    break

# Y방향 회문체크
            if arr[j][i] == arr[j+M-1][i]:
                result = ''
                cnt = 0
                for k in range(M):
                    if arr[j+k][i] == arr[j+M-1-k][i]:
                        result += arr[j+k][i]
                        cnt += 1
                if cnt == M:
                    break
        if cnt == M:
            break

    print(f'#{test_case} {result}')