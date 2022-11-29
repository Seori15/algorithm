# [A] delta 설정
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

# [B] lab2에 0이 있는지 check하면서 최대값을 찾는 check 함수 설정
def check():
    maxV = 0
    for i in range(N):
        for j in range(N):
            if lab2[i][j] == 0:
                return False
            else:
                maxV = max(maxV, lab2[i][j])
    return maxV

from sys import stdin
# [1] 입력값 설정
N, M = map(int, stdin.readline().split())
lab = [[] for _ in '_'*N]
for i in range(N):
    lab[i] = list(map(int, stdin.readline().split()))

# [2] 바이러스 좌표값 저장
viruses = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            viruses.append((i, j))


from itertools import combinations
from collections import deque

# [3] 경우의 수만큼 바이러스를 퍼트린다.
result = N**2
for case in list(combinations(viruses, M)):
    lab2 = [line[:] for line in lab]
    queue = deque([])

    # [3-1] 바이러스를 1로 체크하고 queue에 넣는다.
    for virus in case:
        i, j = virus
        lab2[i][j] = 1
        queue.append((i, j))

    # [3-2] bfs로 바이러스를 퍼트리면서 +1씩 값을 넣어준다.
    visited = [[0]*N for _ in '_'*N]
    while queue:
        i, j = queue.popleft()
        visited[i][j] = 1
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and lab2[ni][nj] != 1:
                if visited[ni][nj]:
                    if lab2[ni][nj] > lab2[i][j] + 1:
                        lab2[ni][nj] = lab2[i][j] + 1
                        queue.append((ni, nj))

                elif not visited[ni][nj]:
                    lab2[ni][nj] = lab2[i][j] + 1
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

    # [3-3] check() 함수를 통해 0이 있는지 확인하고, 최대값을 찾는다.
    flag = check()
    if flag:
        result = min(result, flag)
    else:
        continue

# [4] 출력 설정. result가 갱신되지 않았다면 -1을 출력한다.
if result == N**2:
    print(-1)
else:
    print(result-1)
