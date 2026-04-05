class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        charSet={}
        maxf=0
        for r in range(len(s)):
            charSet[s[r]]=1+charSet.get(s[r],0)
            maxf=max(maxf,charSet[s[r]])
            if (r-l+1)-maxf>k:
                charSet[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            