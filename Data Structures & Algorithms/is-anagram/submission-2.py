class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = [0]*26 , [0]*26
        if len(s)==len(t):
            for i in range(len(s)):
                s1[ord(s[i])-ord('a')]+=1
                s2[ord(t[i])-ord('a')]+=1
            return s1==s2
        return False


        