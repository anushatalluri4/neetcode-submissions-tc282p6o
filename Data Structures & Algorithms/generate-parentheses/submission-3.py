class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, close,curr):
            if open == close == n:
                res.append(curr[:])
                return
            if open<n:
                dfs(open+1,close,curr+"(")
            if close<open:
                dfs(open,close+1,curr+")")
        dfs(0,0,"")
        return res