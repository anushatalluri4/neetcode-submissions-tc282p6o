class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res+=self.pal(s,i,i)
            res+= self.pal(s,i,i+1)
        return res
    def pal(self,s,i,j):
        count = 0
        while i>=0 and j<len(s) and s[i]==s[j]:
            count+=1
            i-=1
            j+=1
        return count