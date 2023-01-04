# [1] 입력값 설정
while True:
    n = int(input())
    if n == 0:
        exit()

    rooms = [[] for _ in '_'*(n+1)]
    for i in range(1, n+1):
        kind, money, *path = list(input().split())
        path.pop()
        rooms[i] = [i, kind, int(money), list(map(int, path))]

    # [2] 1번부터 각 방을 BFS 탐색하면서 방문처리한다.
    from collections import deque
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([rooms[1] + [0]])
    while queue:
        now, kind, money, path, balance = queue.popleft()

        # [2-1] 방의 종류에 따라 예산 및 방문 처리
        if kind == 'E':
            visited[now] = 1

        elif kind == 'L':
            visited[now] = 1
            if balance < money:
                balance = money

        elif kind == 'T':
            if balance >= money:
                balance -= money
                visited[now] = 1
            else:
                continue

        # [2-2] 다음 방 방문
        for next in path:
            if not visited[next]:
                queue.append(rooms[next] + [balance])

    # [3] n번 방에 방문처리 되어있다면 Yes 출력
    print('Yes') if visited[n] == 1 else print('No')