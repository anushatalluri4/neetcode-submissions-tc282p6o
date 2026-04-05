class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()
        islands = 0
        def dfs(r,c):
            stack = [(r,c)]
            visit.add((r,c))
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if row in range(Rows) and col in range(Cols) and grid[row][col] == "1" and (row,col) not in visit:
                        stack.append((row,col))
                        visit.add((row,col))


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands