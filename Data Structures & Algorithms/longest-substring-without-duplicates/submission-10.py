class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        res = 0
        for i in range(len(s)):
            while s[i] in d:
                d.remove(s[l])
                l+=1
            d.add(s[i])
            res = max(res,i-l+1)
        return res