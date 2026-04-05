class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.ind = 0
        for i in range(len(s)):
            self.isPal(s,i,i)
            self.isPal(s,i,i+1)
        return s[self.ind:self.ind+self.maxlen]
    def isPal(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > self.maxlen:
                self.maxlen = r-l+1
                self.ind = l
            l-=1
            r+=1
        