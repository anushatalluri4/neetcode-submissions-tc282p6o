class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        N =  len(intervals)
        intervals.sort()
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1,N):
            if intervals[i][0]<=r:
                r = max(r, intervals[i][1])
            else:
                res.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        res.append([l,r])
        return res