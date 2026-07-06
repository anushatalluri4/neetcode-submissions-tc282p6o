class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        if len(t)>len(s):
            return ""
        for i in range(len(t)):
            d[t[i]] = d.get(t[i],0)+1
        have , need = 0, len(d)
        minWin, minWinLen = [-1,-1], float("inf")
        win = {}
        l=0
        for i in range(len(s)):
            win[s[i]]=win.get(s[i],0)+1
            if s[i] in d and d[s[i]]==win[s[i]]:
                have+=1
            while have==need:
                if i-l+1<minWinLen:
                    minWin = [l,i]
                    minWinLen = i-l+1
                win[s[l]]-=1
                if s[l] in d and d[s[l]]>win[s[l]]:
                    have-=1
                l+=1
        l,r = minWin
        return s[l:r+1] if minWinLen!=float("inf") else ""
