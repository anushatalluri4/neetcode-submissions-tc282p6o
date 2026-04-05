class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        d={}
        res=0
        for r in range(len(s)):
            while s[r] in d:
                d.pop(s[l])
                l+=1
            d[s[r]]=r
            res=max(res,r-l+1)
        return res
        