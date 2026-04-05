class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        area = 0
        for i in range(n+1):
            while stack and (i==n or heights[i]<=heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                area  = max(area,height*width)
            stack.append(i)
        return area