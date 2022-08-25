# 0. DFS 함수 설정
def DFS(i, j):
    global result
    if maze[i][j] == 1:     # 미로에서 벽을 만나면 False 반환
       return False

    elif maze[i][j] == 3:   # 미로에서 도착점을 만나면 result = 1 저장
        result = 1
        return True

    if not visited[i][j]:   # 방문표시 후 maze 범위 내에서 DFS 재귀 탐색
        visited[i][j] = 1

        for (ni, nj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < 16 and 0 < nj < 16:
                DFS(ni, nj)

        visited[i][j] = 0   # 통로가 겹칠 때를 대비해서 방문조건 초기화



# 1. 입력값 설정
for test_case in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    result = 0
    DFS(1, 1)
    print(f'#{test_case} {result}')