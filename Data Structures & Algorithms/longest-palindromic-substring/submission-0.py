class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.ind=0
        self.maxlen=0
        for i in range(len(s)):
            self.getPal(s,i,i)
            self.getPal(s,i,i+1)
        return s[self.ind:self.ind+self.maxlen]

    def getPal(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1) >self.maxlen:
                self.maxlen=r-l+1
                self.ind=l
            l-=1
            r+=1
            
                