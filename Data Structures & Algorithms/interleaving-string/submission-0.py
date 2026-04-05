class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!= len(s1)+len(s2):
            return False
        if len(s2)<len(s1):
            s1,s2 = s2,s1
        dp = [ False ] * (len(s2)+1)
        for i in range(len(s1),-1,-1):
            currRow = [False] * (len(s2)+1)
            if i == len(s1):
                currRow[len(s2)] = True
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i] == s3[i+j] and dp[j]:
                    currRow[j] = True
                if j<len(s2) and s2[j] == s3[i+j] and currRow[j+1]:
                    currRow[j] = True
            dp = currRow
        return dp[0]          