class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charS , charT = [0]*26, [0]*26
        for i in range(len(s)):
            charS[ord(s[i])-ord("a")] +=1
            charT[ord(t[i])-ord("a")] +=1
        return charS==charT
            