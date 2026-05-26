class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s,e = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            if s>intervals[i][1]:
                res.append(intervals[i])
            elif e<intervals[i][0]:
                res.append([s,e])
                return res+intervals[i:]
            else:
                s, e = min(s, intervals[i][0]), max(e,intervals[i][1])
        res.append([s,e])
        return res

