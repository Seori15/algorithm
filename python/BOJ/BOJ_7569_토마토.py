from sys import stdin
# bfs 풀이
# 입력값 설정
M, N, H = map(int, stdin.readline().split())
storage = [[[] for _ in '_' * N] for _ in '_'*H]
for i in range(H):
    for j in range(N):
        storage[i][j] = list(map(int, stdin.readline().split()))

# 토마토가 들어있는 좌표를 queue에 저장한다.
queue = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if storage[i][j][k] == 1:
                queue.append((i, j, k))

# queue에 저장된 좌표에서 6방향을 탐색한다.
# (ni, nj, nk)가 범위 안에 있으며 0이라면 (i, j)값의 +1로 갱신한다.
di = [0, 0, 0, 0, 1, -1]
dj = [0, 1, 0, -1, 0, 0]
dk = [-1, 0, 1, 0, 0, 0]
while queue:
    L = len(queue)
    queue2 = []
    for n in range(L):
        i, j, k = queue[n]
        for dr in range(6):
            ni, nj, nk = i+di[dr], j+dj[dr], k+dk[dr]
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and storage[ni][nj][nk] == 0:
                storage[ni][nj][nk] = storage[i][j][k] + 1
                queue2.append((ni, nj, nk))
    queue = queue2[:]

# storage에 0이 하나라도 남아있으면 -1을 출력해야 한다.
# 그 외에는 가장 숫자가 큰 토마토의 -1이 토마토가 익을 때까지의 최소 날짜이다.
result = 0
zero = 0
for i in range(H):
    for j in range(N):
        result = max(result, max(storage[i][j]))
        if 0 in storage[i][j]:
            zero = 1

if zero:
    print(-1)
else:
    print(result-1)