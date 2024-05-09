class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
		# [1] 변수 설정
        m, n = len(grid[0]), len(grid)
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        fresh = 0
        rottens = deque()
        
        # [2] fresh orange의 존재 유무, rotten orange의 좌표 저장
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh = 1
                elif grid[i][j] == 2:
                    rottens.append((i, j))
        
        # [3] 반례 처리 1. fresh orange가 없는 경우
        if not fresh:
            return 0
        
        # [4] rotten orange로부터 BFS 탐색으로 fresh orange를 만나면 자신의 값 + 1로 갱신
        while rottens:
            i, j = rottens.popleft()
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    rottens.append((ni, nj))
                    grid[ni][nj] = grid[i][j] + 1

		# [5] fresh orange가 남아있는 경우 불가능으로 판단하여 -1 반환
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

		# [6] fresh orange가 없다면 가장 큰 값의 -2(모두 썩는 데 걸린 시간) 반환
        return max(map(max, grid)) - 2