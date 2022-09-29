from sys import stdin
# bfs 풀이
# 입력값 설정
M, N = map(int, stdin.readline().split())
storage = [[] for _ in '_'*N]
for i in range(N):
    storage[i] = list(map(int, stdin.readline().split()))

# 토마토가 들어있는 좌표를 queue에 저장한다.
queue = []
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            queue.append((i, j))

# queue에 저장된 좌표에서 4방향을 탐색한다.
# (ni, nj)가 범위 안에 있으며 0이라면 (i, j)값의 +1로 갱신한다.
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
while queue:
    L = len(queue)
    queue2 = []
    for n in range(L):
        i, j = queue[n]
        for dr in range(4):
            ni, nj = i + di[dr], j + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and storage[ni][nj] == 0:
                storage[ni][nj] = storage[i][j] + 1
                queue2.append((ni, nj))
    queue = queue2[:]

# storage에 0이 하나라도 남아있으면 -1을 출력해야 한다.
# 그 외에는 가장 숫자가 큰 토마토의 -1이 토마토가 익을 때까지의 최소 날짜이다.
result = 0
zero = 0
for i in range(N):
    result = max(result, max(storage[i]))
    if 0 in storage[i]:
        zero = 1

if zero:
    print(-1)
else:
    print(result-1)