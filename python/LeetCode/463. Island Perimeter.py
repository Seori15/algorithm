#문제 풀이
"""
이 문제 조건에서 섬은 단 하나만 존재한다. 
따라서, 육지인 좌표를 찾아 dfs 탐색을 실행하면 모든 육지 타일을 탐색할 수 있다.
섬의 perimeter를 구하기 위해 각 육지 타일에서 바다 및 지평선과의 경계가 맞닿는 수를 구한다.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
		    # [A] grid에서 첫 육지 타일을 찾아주는 함수
        def findFirstLandCell(grid: List[List[int]]) -> tuple:
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1:
                        return i, j

				# [B] DFS 탐색을 통해 육지와 바다/지평선의 경계를 구하는 함수
        def dfs(i: int, j: int, grid: List[List[int]]) -> int:
            border = 0
            visited[i][j] = 1
            for di, dj in direction:
                ni, nj = i+di, j+dj
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj]:
                    if not visited[ni][nj]:
                        border += dfs(ni, nj, grid)
                else:
                    border += 1
            return border
        
        # [1] DFS를 탐색을 위한 사전 설정
        row, col = len(grid), len(grid[0])                      # grid의 row 수, column 수
        visited = [[0 for _ in range(col)] for _ in range(row)] # 중복 탐색 방지를 위한 visited 리스트
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]          # DFS 탐색할 4방향 좌표를 담은 리스트

				# [2] 육지 타일을 찾아, DFS 탐색 실시
        i, j = findFirstLandCell(grid)
        return dfs(i, j, grid)