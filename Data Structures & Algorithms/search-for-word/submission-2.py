class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r,c,i): # position in board and current index in word
            if i == len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i] or board[r][c] =="#":
                return False
            temp = board[r][c]
            board[r][c] = "#"
            res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
            board[r][c]=temp
            return res
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False
