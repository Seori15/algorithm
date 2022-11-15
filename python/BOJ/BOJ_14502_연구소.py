from itertools import combinations
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# [1] 입력값 설정
N, M = map(int, input().split())
arr = [[] for _ in '_'*N]
for i in range(N):
    arr[i] = list(map(int, input().split()))

viruses = []
safe = []
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            viruses.append((i, j))
        elif arr[i][j] == 0:
            safe.append((i, j))
            answer += 1

combs = list(combinations(safe, 3))

# combinations 갯수만큼 반복
mincnt = answer
for n in range(len(combs)):
    # 새로운 맵 arr2 생성
    arr2 = [[] for _ in '_'*N]
    for i in range(N):
        arr2[i] = arr[i][:]

    # 벽 3개 세우기
    for comb in combs[n]:
        i, j = comb
        arr2[i][j] = 1

    # 바이러스 확산
    cnt = 0
    queue = deque(viruses)
    while queue:
        i, j = queue.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr2[ni][nj] == 0:
                arr2[ni][nj] = 2
                cnt += 1
                queue.append((ni, nj))

    # 확산된 virus 개수만큼 cnt하면서 최소값 찾기
    mincnt = min(cnt, mincnt)

# 확산된 virus 최솟값과, 벽을 세운 3을 ans에서 빼면 최대값
print(answer-3-mincnt)