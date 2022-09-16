DFS 풀이
# 이동 가능한 방의 개수를 찾는 함수 설정
def move(i, j):
    global cnt
    for n in direction:
        if 0 <= i + dx[n] < N and 0 <= j + dy[n] < N:
            if arr[i + dx[n]][j + dy[n]] == arr[i][j] + 1:
                cnt += 1
                move(i + dx[n], j + dy[n])

# 입력값 설정
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = [0, 1, 2, 3] # 상 하 좌 우

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in '_'*N]

    cntM = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            move(i, j)

            # move 함수를 돌고 나서, cnt 값이 크다면 cnt와 방 번호를 저장
            if cntM < cnt:
                cntM = cnt
                room = arr[i][j]
            # cnt 값이 같다면 작은 방 번호를 저장
            elif cntM == cnt:
                if room > arr[i][j]:
                    room = arr[i][j]
    print(f'#{test_case} {room} {cntM}')

------------------------------------------
1차원 리스트 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 방 개수만큼의 rooms 리스트를 만들어두고 각 방 번호에 좌표를 할당한다.
    rooms = [[] for _ in '_' * (N ** 2)]
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            rooms[arr[j] - 1] = [i, j]

    cnt = 1
    cntM = 0
    idx = 0
    # 끝방부터 역순으로 탐색한다. 앞방과의 거리가 1이라면 cnt + 1
    for i in range(N ** 2 - 1, 0, -1):
        if abs(rooms[i][0] - rooms[i - 1][0]) + abs(rooms[i][1] - rooms[i - 1][1]) == 1:

            cnt += 1

            # 1번방일 경우 cntM값 비교하여 저장.
            if i == 1:
                if cntM <= cnt:
                    cntM = cnt
                    idx = 1

        # 거리가 1이 아니라면 cntM값을 비교하여 저장 후 초기화
        else:
            if cntM <= cnt:
                cntM = cnt
                idx = i + 1
                cnt = 1
            cnt = 1

    print(f'#{test_case} {idx} {cntM}')