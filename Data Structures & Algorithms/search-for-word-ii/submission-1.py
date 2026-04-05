class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]
        rows, cols = len(board), len(board[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or visited[r][c]:
                return False
            visited[r][c]=True
            res=(dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                 dfs(r,c-1,i+1))
            visited[r][c]=False
            return res
        for word in words:
            flag=False
            for r in range(rows):
                if flag:
                    break
                for c in range(cols):
                    if dfs(r,c,0):
                        res.append(word)
                        flag=True
                        break
        return res
