class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q=deque()
        res = [0]*len(temperatures)
        for r in range(len(temperatures)):
            while q and temperatures[r]>temperatures[q[-1]]:
                ind = q.pop()
                res[ind] = r-ind
            q.append(r)
        return res