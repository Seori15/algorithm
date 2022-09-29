# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# x와 y방향으로, 1이 연속되는 횟수를 저장
    result = 0
    countx = 1
    county = 1
    count_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if j + 1 < N and arr[i][j+1] == 1:
                    countx += 1
                else:
                    count_list.append(countx)
                    countx = 1

            if arr[j][i] == 1:
                if j + 1 < N and arr[j+1][i] == 1:
                    county += 1
                else:
                    count_list.append(county)
                    county = 1

# 연속 횟수가 K만큼 있던 경우 result +1
    for i in count_list:
        if i == K:
            result += 1

    print(f'#{test_case} {result}')
