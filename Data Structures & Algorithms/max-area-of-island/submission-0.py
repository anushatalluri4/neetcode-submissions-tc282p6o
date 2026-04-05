class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        Directions = [[1,0],[0,1],[-1,0],[0,-1]]
        self.maxarea = 0
        islands = 0
        def dfs(r,c):
            area = 1
            stack = [(r,c)]
            visited.add((r,c))
            while stack:
                row, col = stack.pop()
                for dr, dc in Directions:
                    nr, nc = dr+row, dc+col
                    if nr in range(Rows) and nc in range(Cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        stack.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            self.maxarea = max(self.maxarea,area)
            print(self.maxarea)
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        print("islands" + str(islands))
        return self.maxarea
