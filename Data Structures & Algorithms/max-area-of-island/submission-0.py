class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0 

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0 
            area = 1 

            while q:
                curr_r, curr_c = q.popleft() 
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc 

                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == 1): 
                        
                        area += 1 
                        grid[nr][nc] = 0 
                        q.append((nr, nc))
            
            return area
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        
        return ans 
