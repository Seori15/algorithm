def solution(info, edges):
    L = len(info)
    visited = [0]*L
    visited[0] = 1
    answer = []

    # dfs 함수 설정
    def dfs(sheep, wolves):
        if sheep > wolves:
            answer.append(sheep)
        else:
            return

        for edge in edges:
            par = edge[0]
            ch = edge[1]
            if not visited[ch] and visited[par]:
                visited[ch] = 1
                if info[ch] == 0:
                    dfs(sheep+1, wolves)
                elif info[ch] == 1:
                    dfs(sheep, wolves+1)
                visited[ch] = 0

    dfs(1, 0)
    return max(answer)