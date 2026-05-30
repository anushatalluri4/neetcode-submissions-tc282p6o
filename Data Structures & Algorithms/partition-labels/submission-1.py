class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        res = []
        for i, c in enumerate(s):
            d[c]=i
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(end, d[s[i]])
            if  i == end:
                res.append(size)
                size = 0
        return res