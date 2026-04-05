class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        countT, countS = {}, {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        have, need = 0, len(countT)
        minWin, minWinLen = [-1,-1], float("infinity")
        window = {}
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < minWinLen:
                    minWinLen = r-l+1
                    minWin = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l, r = minWin
        return s[l:r+1] if minWinLen != float("infinity") else ""