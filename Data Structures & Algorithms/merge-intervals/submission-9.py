class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        s, e = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            if s>intervals[i][1]:
                res.append(intervals[i])
            elif e<intervals[i][0]:
                res.append([s,e])
                s, e = intervals[i][0], intervals[i][1]
            else:
                s, e = min(s,intervals[i][0]), max(e,intervals[i][1])
        res.append([s,e])
        return res