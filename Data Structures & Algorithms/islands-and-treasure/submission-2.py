class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = dr+row, dc+col
                if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]>grid[row][col]+1:
                    grid[nr][nc]=grid[row][col]+1
                    q.append((nr,nc))