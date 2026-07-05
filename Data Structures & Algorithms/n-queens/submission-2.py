class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posD = set()
        negD = set()
        board = [["."]*n for i in range(n)]
        res = []
        def dfs(r):
            if r == n:
                res.append(["".join(s) for s in board])
                return
            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res

