class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                ind = stack.pop()
                res[ind] = t - ind
            stack.append(t)
        return res
