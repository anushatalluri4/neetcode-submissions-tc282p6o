class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        if len(s)<len(t):
            return ""
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        l, r = 0, 0
        minwin, winlen = [-1,-1], float("inf")
        have, need = 0, len(countT)
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if winlen > r-l+1:
                    minwin = [l,r]
                    winlen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = minwin
        return s[l:r+1] if minwin != float("inf") else ""
                