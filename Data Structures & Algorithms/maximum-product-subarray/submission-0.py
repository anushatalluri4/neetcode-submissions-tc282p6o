class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res=max(nums)
        for i in nums:
            tmp=currMax * i
            currMax=max(i,i*currMax,i*currMin)
            currMin=min(i,i*currMin,tmp)
            res=max(res,currMax)
        return res
