class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        if len(t)>len(s):
            return ""
        countt = {}
        for i in range(len(t)):
            countt[t[i]] = 1+countt.get(t[i],0)
        win = {}
        l=0
        have, need = 0, len(countt)
        minWin, minWinLen = [-1,-1], float("inf")
        for i in range(len(s)):
            win[s[i]] = 1+win.get(s[i],0)
            if s[i] in countt and countt[s[i]] == win[s[i]]:
                have+=1
            while have == need:
                if (i-l+1)<minWinLen:
                    minWinLen = i-l+1
                    minWin = [l,i]
                win[s[l]]-=1
                if s[l] in countt and countt[s[l]] > win[s[l]]:
                    have-=1
                l+=1
        l, r = minWin
        return s[l:r+1] if minWinLen != float("inf") else ""
