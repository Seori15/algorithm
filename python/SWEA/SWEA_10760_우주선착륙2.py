# [A] 8방향 delta 설정
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# [1] 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (M + 2)] + [[] for _ in '_' * N] + [[0] * (M + 2)]
    for i in range(1, N + 1):
        arr[i] = [0] + list(map(int, input().split())) + [0]

    # [2] 높이가 낮은 칸이 4칸 이상인 곳을 탐색
    result = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            possible = 0
            for (di, dj) in delta:
                ni, nj = i + di, j + dj
                if arr[ni][nj] and arr[ni][nj] < arr[i][j]:
                    possible += 1
                    if possible == 4:
                        result += 1
                        break

    print(f'#{test_case} {result}')