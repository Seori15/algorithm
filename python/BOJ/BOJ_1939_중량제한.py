from collections import deque

# [A] bfs 함수 정의
def bfs(mid):
    # [A-1] 이 bfs 탐색은 시작점 S에서 시작한다.
    queue = deque([S])
    while queue:
        now = queue.popleft()

        # [A-2] bfs 탐색하면서 도착점 E에 도달하면 True를 반환한다.
        if now == E:
            return True

        # [A-3] 현재 지점 now에서 연결된 (next, cost)를 찾는다.
        #       next가 방문하지 않았으며 cost가 mid 이상일 경우에만 append한다.
        for (next, cost) in adjL[now]:
            if not visited[next] and mid <= cost:
                visited[next] = 1
                queue.append(next)

    # [A-4] A-3 조건에 걸러져 도착하지 못한 경우(= cost가 mid 미만) False를 반환한다.
    return False

# [1] 입력값 설정
N, M = map(int, input().split())
adjL = [[] for _ in '_'*(N+1)]
for _ in '_'*M:
    A, B, C = map(int, input().split())
    adjL[A].append((B, C))
    adjL[B].append((A, C))
S, E = map(int, input().split())

# [2] 이분 탐색 풀이
low = 1
top = 1000000000

# [2-1] mid라는 이분 탐색 인자로 중량 최댓값을 구한다.
while low <= top:
    visited = [0]*(N+1)
    mid = (top + low) // 2

    # [2-2] bfs 탐색 결과 True라면 mid 값을 크게 할 필요가 있다.
    if bfs(mid):
        low = mid + 1
    # [2-3] bfs 탐색 결과 False라면 mid 값을 줄여야 한다.
    else:
        top = mid - 1
print(top)