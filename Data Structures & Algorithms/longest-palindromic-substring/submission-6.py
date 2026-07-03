class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.maxlen = 0
        for i in range(len(s)):
            self.pal(s,i,i)
            self.pal(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
    def pal(self, s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            if j-i+1>self.maxlen:
                self.maxlen = j-i+1
                self.start = i
            i-=1
            j+=1
    