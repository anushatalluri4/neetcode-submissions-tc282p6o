class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols  = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = collections.deque()
        fresh = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        lev = 0
        while fresh>0 and q:
            leng = len(q)
            for i in range(leng):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr in range(Rows) and nc in range(Cols) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            lev += 1
        return lev if not fresh else -1
    