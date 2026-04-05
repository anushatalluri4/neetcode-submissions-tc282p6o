class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        l,r=0,len(heights)-1
        while(l<r):
            area=min(heights[l],heights[r])*(r-l)
            max_water=max(max_water,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_water


        