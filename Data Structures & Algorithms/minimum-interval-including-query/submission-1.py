class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        minh = []
        res = {}
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q:
                s,e = intervals[i][0], intervals[i][1]
                heapq.heappush(minh,(e-s+1,e))
                i+=1
            while minh and minh[0][1]<q:
                heapq.heappop(minh)
            res[q] = minh[0][0] if minh else -1
        return [res[q] for q in queries]
