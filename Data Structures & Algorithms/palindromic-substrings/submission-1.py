class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res=0
        for i in range(len(s)):
            self.countPal(s,i,i)
            self.countPal(s,i,i+1)
        return self.res
    def countPal(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            self.res+=1
            l-=1
            r+=1
        
