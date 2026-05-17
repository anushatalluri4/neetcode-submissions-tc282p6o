class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                ind, hei = stack.pop()
                maxarea = max(maxarea,(i-ind)*hei)
                start = ind
            stack.append((start,h))
        for i, h in stack:
            maxarea = max(maxarea,(len(heights)-i)*h)
        return maxarea