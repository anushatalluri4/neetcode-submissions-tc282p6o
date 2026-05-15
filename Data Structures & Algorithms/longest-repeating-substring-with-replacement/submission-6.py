class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        maxf = 0
        res = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0)+1
            maxf = max(maxf,d[s[r]])
            if r-l+1-maxf>k:
                d[s[l]]-=1
                l+=1
            res = r-l+1
        return res