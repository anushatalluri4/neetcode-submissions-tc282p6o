class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        l, r = 0,0
        res = 0
        while r<len(s):
            if s[r] not in d:
                res = max(res,r-l+1)
                d.add(s[r])
                r+=1
            else:
                d.remove(s[l])
                l+=1
        return res