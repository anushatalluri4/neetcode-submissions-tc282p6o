class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1]>heights[i]:
                ind, hei = stack.pop()
                maxarea = max(maxarea,hei*(i-ind))
                start = ind
            stack.append((start,heights[i]))
        for s,h in stack:
            maxarea = max(maxarea, h*((len(heights)-s)))
        return maxarea
