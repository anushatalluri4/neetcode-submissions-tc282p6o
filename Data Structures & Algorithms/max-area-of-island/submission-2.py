class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        maxarea = 0
        def dfs(r,c):
            if r not in range(Rows) or c not in range(Cols) or grid[r][c] != 1 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1+dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
                
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    maxarea = max(maxarea,dfs(r,c))
        return maxarea
