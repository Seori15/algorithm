"""
체스판에서 나이트가 밟아야 할 x번째 발판의 좌표(i, j)를 steps 1차원 리스트에 담는다.
steps에 담긴 x번째 발판의 좌표(i, j)에서 x+1번째 발판의 좌표(ni, nj)로 나이트가 이동 가능하지 않다면 False를 return한다.

테스트케이스 1025번에서는 0번째 step이 (0, 0)이 아니므로 False 처리가 필요하다.
"""
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        # [0] T/C 1025 예외처리				
        if grid[0][0]: return False
        
        # [1] steps 리스트에 각 x번째 step의 좌표(i, j)를 저장한다.
        n = len(grid)
        steps = [0 for _ in range(n**2)]
        for i in range(n):
            for j in range(n):
                step = grid[i][j]
                steps[step] = (i, j)

        # [2] 현재 step(i, j)에서 다음 step(ni, nj)로 나이트가 이동한지 체크
        #     거리가 3이고 i, ni나 j, nj가 같지 않아야 한다.
        for step in range(len(steps)-1):
            i, j = steps[step]
            ni, nj = steps[step + 1]
            if i == ni or j == nj or abs(ni - i) + abs(nj - j) != 3:
                return False
        return True
        
  
  
# DFS 풀이
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        # [0] T/C 1025 예외처리				
        if grid[0][0]: return False
		
        # [1] DFS 변수 설정
        n = len(grid)   # 가로세로 길이
        fin = n**2 - 1  # 마지막 발판 숫자
        direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)] # 나이트의 이동 방향

        # [2] DFS 탐색 시작
        def dfs(now: int, i: int, j: int, grid: List[List[int]]) -> bool:

            # [2-1] 종료조건. 마지막 발판에 도달했을 때, True 반환
            if now == fin:
                return True

            # [2-2] 나이트의 이동 범위에 다음 발판이 있다면 DFS 탐색, 없다면 False 반환
            next = now + 1
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == next:
                    return dfs(next, ni, nj, grid)
            else:
                return False

        return dfs(0, 0, 0, grid)