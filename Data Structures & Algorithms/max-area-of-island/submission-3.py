class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        visit = set()
        def dfs(r,c):
            res = 1
            stack = [(r,c)]
            visit.add((r,c))
            while stack:
                row,col = stack.pop()
                for dr,dc in directions:
                    nr,nc = dr+row, dc+col
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1 and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        stack.append((nr,nc))
                        res+=1
                        print(res)
            return res
        maxarea = 0      
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxarea = max(maxarea,dfs(r,c))
                    print(maxarea)

        return maxarea