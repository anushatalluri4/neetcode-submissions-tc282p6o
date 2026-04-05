class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.ind = 0
        self.maxlen = 0 
        for i in range(len(s)):
            self.ispal(i,i,s)
            self.ispal(i,i+1,s)
        return s[self.ind:self.ind+self.maxlen]
    def ispal(self,l,r,s):
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > self.maxlen:
                self.maxlen = r-l+1
                self.ind = l
            l-=1
            r+=1
        
