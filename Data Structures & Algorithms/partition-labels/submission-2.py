class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        end = 0
        size = 0
        res = []
        for i in range(len(s)):
            end = max(end,d[s[i]])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res
            