class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxsumend=nums[0]
        for i in range(1,len(nums)):
            maxsumend=max(maxsumend+nums[i],nums[i])
            res=max(maxsumend,res)
        return res            