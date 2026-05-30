class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax, currmin = 1, 1
        res = max(nums)
        for num in nums:
            temp = currmax*num
            currmax = max(currmax*num, num, currmin*num)
            currmin = min(temp,num,currmin*num)
            res = max(res,currmax)
        return res