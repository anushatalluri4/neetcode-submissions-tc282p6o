class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currmax = nums[0]
        for i in range(1,len(nums)):
            currmax = max(currmax+nums[i],nums[i])
            res = max(res,currmax)
        return res