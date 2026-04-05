class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        N =  len(intervals)
        l, r = newInterval[0], newInterval[1]
        for i in range(N):
            if r<intervals[i][0]:
                res.append([l,r])
                return res+intervals[i:]
            elif l>intervals[i][1]:
                res.append(intervals[i])
            else:
                l, r = min(l, intervals[i][0]), max(r, intervals[i][1])
        res.append([l,r])
        return res