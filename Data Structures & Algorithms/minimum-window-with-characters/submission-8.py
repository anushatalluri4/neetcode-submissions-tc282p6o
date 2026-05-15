class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i],0) + 1
        minwin, minwinlen = [-1,-1], float("inf")
        have, need = 0, len(countT)
        win = {}
        l = 0
        for r in range(len(s)):
            win[s[r]] = win.get(s[r],0)+1
            if s[r] in countT and countT[s[r]]==win[s[r]]:
                have +=1
            while have == need:
                if r-l+1<minwinlen:
                    minwinlen = r-l+1
                    minwin = [l,r]
                win[s[l]]-=1
                if s[l] in countT and countT[s[l]]>win[s[l]]:
                    have -= 1
                l+=1
        l, r = minwin
        return s[l:r+1] if minwinlen!=float("inf") else ""

