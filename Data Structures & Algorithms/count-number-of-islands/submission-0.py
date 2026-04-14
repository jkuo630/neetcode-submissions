class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through the graph 
        # if theres a 1, increase numislands by 1 
        # bfs to all the 1s changing them to 0s 
        ans = 0 

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if (
                        (row + dr) in range(rows) and 
                        (col + dc) in range(cols) and 
                        grid[row + dr][col + dc] == "1"
                    ):
                        grid[row+dr][col+dc] = "0"
                        q.append((row + dr, col + dc))

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    ans += 1 
                    bfs(r, c)
        
        return ans 