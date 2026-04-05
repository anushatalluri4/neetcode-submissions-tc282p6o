class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        for ind, height in enumerate(heights):
            start = ind
            while stack and stack[-1][1]>height:
                index, hei = stack.pop()
                maxarea = max(maxarea,hei*(ind-index))
                start = index
            stack.append((start,height))
        for i, h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea
