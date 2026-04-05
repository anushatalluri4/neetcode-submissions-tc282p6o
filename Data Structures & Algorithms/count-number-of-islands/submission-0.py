class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()

        def dfs(r,c):
            q=[(r,c)]
            visited.add((r,c))
            while q:
                row, col=q.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1
        return islands