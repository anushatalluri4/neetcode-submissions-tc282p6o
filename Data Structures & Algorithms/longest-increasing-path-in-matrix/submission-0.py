class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dp = {}
        def dfs(r,c,prev):
            if r not in range(rows) or c not in range(cols) or matrix[r][c]<=prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res = max(res, 1+ dfs(r+1,c,matrix[r][c]))
            res = max(res, 1+ dfs(r-1,c,matrix[r][c]))
            res = max(res, 1+ dfs(r,c+1,matrix[r][c]))
            res = max(res, 1+ dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res
        for row in range(rows):
            for col in range(cols):
                dfs(row,col,-1)
        return max(dp.values())
