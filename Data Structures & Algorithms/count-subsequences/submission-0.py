class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0]*(n+1)
        nextDP = [0] *(n+1)
        dp[n] = nextDP[n] = 1
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                nextDP[j] = dp[j]
                if s[i] == t[j]:
                    nextDP[j] += dp[j+1]
            dp = nextDP[:]
        return dp[0]