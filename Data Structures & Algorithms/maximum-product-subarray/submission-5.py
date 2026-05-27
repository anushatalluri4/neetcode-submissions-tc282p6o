class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax, currmin = 1,1
        res = max(nums)
        for i in nums:
            temp = currmax*i
            currmax = max(currmax*i,i,currmin*i)
            currmin = min(temp,i,currmin*i)
            res = max(res,currmax)
        return res