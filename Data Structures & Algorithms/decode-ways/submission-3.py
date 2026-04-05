class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = number of ways to decode i 
        # dp1 = number of ways to decode i+1
        # dp2 = number of ways to decode i+2
        dp, dp2 = 0, 0
        dp1 = 1 # corresponds to len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp += dp2
            dp,dp1,dp2 = 0,dp,dp1
        return dp1
