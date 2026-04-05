class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        if len(t)>len(s):
            return ""
        countT = {}
        win = {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        have, need = 0, len(countT)
        minWinLen, minWin = float("inf"), [-1,-1]
        l, r = 0,0
        while r < len(s):
            win[s[r]] = 1 + win.get(s[r],0)
            if s[r] in countT and win[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < minWinLen:
                    minWinLen = r-l+1
                    minWin = [l,r]
                win[s[l]] -= 1
                if s[l] in countT and win[s[l]]<countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = minWin
        return s[l:r+1] if minWinLen!=float("inf") else ""
