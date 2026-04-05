class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackt,stackind = stack.pop()
                res[stackind]=i-stackind
            stack.append((t,i))
        return res
        
                
                

