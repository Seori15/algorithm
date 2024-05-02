"""
0번 방부터 시작하여 얻는 열쇠 순서대로 간 적 없는 다음 방을 방문한다.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    
        # [0] DFS 풀이
        def dfs(start: int, rooms: List[List[int]]) -> None:    
        # [1] 재귀 종료 조건
            if key >= n:
                return
                        
            if visited[room]:
                return
                            
        # [2] 재귀 로직? 내용?
            for key in rooms:
                dfs(key, rooms)
        
        
        
            # [A] 키를 얻어 다음 방을 탐색하는 dfs 함수 작성
            def dfs(start: int, rooms: List[List[int]]) -> None:
                visited[start] = 1
                for next in rooms[start]:
                    if next < n and not visited[next]:
                        dfs(next, rooms)
            
            # [1] DFS를 위한 세팅
            n = len(rooms)                  # 문제에서 주어지는 방의 개수 n
            visited = [0 for _ in range(n)] # 0부터 n까지의 방에 방문했는지 기록할 리스트
            dfs(0, rooms)
            
            # [2] DFS 탐색 이후 visited의 합이 n과 같은지를 반환
            return sum(visited) == n