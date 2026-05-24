class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set()
        negDig = set()
        res = []
        board = [["."]*n for i in range(n)]
        def dfs(r):
            if r == n:
                res.append(["".join(s) for s in board])
                return
            for c in range(n):
                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue
                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res
