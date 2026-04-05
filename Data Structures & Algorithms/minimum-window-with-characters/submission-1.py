class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT,window={},{}
        for i in t:
            countT[i]=1+countT.get(i,0)
        l=0
        minWin, minWinLen = [-1,-1], float("infinity")
        have, need = 0, len(countT)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in countT and countT[s[r]]==window[s[r]]:
                have+=1
            while have == need:
                if (r-l+1)<minWinLen:
                    minWin=[l,r]
                    minWinLen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=minWin
        return s[l:r+1] if minWinLen != float("infinity") else ""
           


        