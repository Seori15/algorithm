from sys import stdin

# 1. 최단거리의 먹이를 찾는 find 함수 설정
# 상어(si, sj)에서 최단경로에 있고 조건에 맞는 먹이(mi, mj)를 찾는다.
def find(si, sj):
    global mi, mj, baby, result
    candidate = []
    visited = [[0]*N for _ in '_'*N]
    cnt = 1
    q = [(si, sj)]
    # q를 갱신할 때마다 cnt +1되면서, 조건에 맞다면 candidate에 추가
    while q:
        L = len(q)
        q2 = []
        for n in range(L):
            (i, j) = q[n]
            for dr in range(4):
                ni, nj = i+di[dr], j+dj[dr]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and space[ni][nj] <= baby:
                    visited[ni][nj] = 1
                    q2.append((ni, nj))
                    if 0 < space[ni][nj] < baby and space[ni][nj] != 9: # ※ 메갈로돈 방지
                        candidate.append((ni, nj))

        # candidate에 추가된게 있다면 정렬 후 mi, mj 타겟 설정
        if len(candidate):
            candidate.sort(key=lambda x: (x[0], x[1]))
            (mi, mj) = candidate[0]
            result += cnt
            return True

        q = q2[:]
        cnt += 1
    # bfs 끝나도 candidate가 없으면 종료
    return False

# 2. 물고기를 먹는 eat 함수 설정
def eat(mi, mj):
    global si, sj, full, baby
    # 상어의 좌표를 옮기고 full +1
    space[si][sj] = 0
    space[mi][mj] = 9
    si, sj = mi, mj
    full += 1
    # 배부른 상어 레벨업
    if full == baby:
        full = 0
        baby += 1


# 입력값 설정
N = int(stdin.readline())
space = [list(map(int, stdin.readline().split())) for _ in '_'*N]
full = 0
baby = 2
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
meal_list = []
result = 0

# 맨 처음 아기상어와 물고기 위치 확인
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            si, sj = i, j
        elif space[i][j] != 0:
            meal_list.append((i, j, space[i][j]))

# find 함수에서 먹을 물고기를 찾았다면 먹고, 없다면 종료
while True:
    if find(si, sj):
        eat(mi, mj)

    else:
        break

print(result)