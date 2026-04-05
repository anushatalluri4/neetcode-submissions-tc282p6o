class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        l, r = 0, 0
        res = 0
        while r<len(s):
            if s[r] in d:
                d.remove(s[l])
                l += 1
            else:
                d.add(s[r])
                res = max(res,r-l+1)
                r+=1
        return res
            