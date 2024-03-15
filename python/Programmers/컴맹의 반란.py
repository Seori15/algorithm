def solution(n, connect):
		# [1] pc라는 2차원 배열에 각 pc간의 연결 관계를 담는다.
    pc = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for u, v in connect:
        pc[u][v] = 1
        pc[v][u] = 1
    
    # [2] pc에서 1과 연결된 컴퓨터를 visited를 활용하여 찾는다.
    visited = [0 for _ in range(n+1)]
    queue = [1]
    while queue:
        start = queue.pop(0)
        visited[start] = 1
        for next in range(1, n+1):
            if pc[start][next] == 1 and not visited[next]:
                queue.append(next)
    
    return sum(visited)