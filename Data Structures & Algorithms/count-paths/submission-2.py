class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for r in range(m-1):
            nextRow = [1]*n
            for c in range(n-2,-1,-1):
                nextRow[c] = nextRow[c+1]+row[c]
            row = nextRow
        return row[0]