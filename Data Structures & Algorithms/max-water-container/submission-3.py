class Solution:
    def maxArea(self, heights: List[int]) -> int:
        marea = 0
        l, r = 0, len(heights)-1
        while l<r:
            area = (r-l)*min(heights[l],heights[r])
            marea = max(marea,area)
            if heights[l]>heights[r]:
                r -= 1
            else:
                l+=1
        return marea