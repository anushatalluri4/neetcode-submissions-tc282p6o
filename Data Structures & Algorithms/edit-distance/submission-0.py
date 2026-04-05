class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1), len(word2)
        if m<n:
            m , n = n, m
            word1, word2 = word2, word1
        dp = [0 for i in range(n+1)]
        nextDP = [0 for i in range(n+1)]
        for i in range(n+1):
            dp[i] = n-i
        for i in range(m-1,-1,-1):
            nextDP[n] = m-i
            for j in range(n-1,-1,-1):
                if word1[i] == word2[j]:
                    nextDP[j] = dp[j+1]
                else:
                    nextDP[j] = 1 + min(dp[j],nextDP[j+1],dp[j+1])
            dp = nextDP[:]
        return dp[0]
