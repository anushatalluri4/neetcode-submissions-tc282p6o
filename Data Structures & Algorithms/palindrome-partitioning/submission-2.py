class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part, res = [], []
        def dfs(i):
            if i>=len(s):
                res.append(part[:])
                return
            for j in range(i,len(s)):
                if self.ispal(i,j,s):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def ispal(self, i,j,s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True