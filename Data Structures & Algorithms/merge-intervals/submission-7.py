class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()
        s,e = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=e:
                e = max(e,intervals[i][1])
            else:
                res.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]
        res.append([s,e])
        return res