def solution(n, k, acquaintance):
		# [1] 2차원 배열 connect에 학생의 지인관계를 저장한다.
    connect = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for u, v in acquaintance:
        connect[u][v] = 1
        connect[v][u] = 1
		
		# [2] visited를 최댓값인 101로 선언해놓고, 1번 학생부터 소문을 전달한다.
		#     소문을 전달하는 과정에서 visited값을 최소값으로 갱신한다.
    visited = [101 for _ in range(n+1)]
    visited[1] = 0
    queue = [1]
    while queue:
        start = queue.pop(0)
        for next in range(1, n+1):
            if connect[start][next]:
                if visited[next] == 101:
                    visited[next] = visited[start]+1
                    queue.append(next)
                elif visited[next] > visited[start]+1:
                    visited[next] = visited[start]+1
                    queue.append(next)

		# [3] k 학생이 소문을 들은 최소값은 visited[k]이며, 듣지 못했을 경우 값은 101이다.
    if visited[k] == 101:
        visited[k] = -1
    return visited[k]