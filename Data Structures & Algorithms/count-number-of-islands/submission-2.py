class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        islands = 0
        def dfs(r,c):
            stack = [(r,c)]
            visited.add((r,c))
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] =="1" and (nr,nc) not in visited:
                        stack.append((nr,nc))
                        visited.add((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1
        return islands