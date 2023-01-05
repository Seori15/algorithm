from collections import deque
def solution(n, wires):

    # [A] 각 출발점에서 연결된 송전탑 개수를 반환하는 bfs 함수
    def bfs(N):
        cnt = 1
        queue = deque([N])
        while queue:
            now = queue.popleft()
            for next in adjL[now]:
                if not visited[next]:
                    visited[next] = 1
                    queue.append(next)
                    cnt += 1
        return cnt

    # [1] wires 연결관계를 adjL에 저장
    adjL = [[] for _ in '_' * (n + 1)]
    for wire in wires:
        A, B = wire
        adjL[A].append(B)
        adjL[B].append(A)

    # [2] wires의 각 wire를 하나씩 끊어본다고 가정하여 완전탐색.
    #     wire의 A와 B를 visited처리하고 bfs 탐색하면 각각 연결된 송전탑만 셀 수 있다.
    answer = 100
    for wire in wires:
        A, B = wire
        visited = [0] * (n + 1)
        visited[A] = 1
        visited[B] = 1
        answer = min(answer, abs(bfs(A) - bfs(B)))

    return answer