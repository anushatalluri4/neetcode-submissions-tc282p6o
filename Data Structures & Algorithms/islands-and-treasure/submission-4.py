class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            nr,nc = q.popleft()
            for dr, dc in directions:
                r,c = nr+dr, nc+dc
                if r>=0 and r<rows and c>=0 and c<cols and grid[r][c]>grid[nr][nc]+1:
                    grid[r][c] = grid[nr][nc]+1
                    q.append((r,c))
        

