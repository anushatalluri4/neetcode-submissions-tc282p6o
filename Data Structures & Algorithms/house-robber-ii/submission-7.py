class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        return max(self.robb(nums[1:]),self.robb(nums[:-1]))
        
    def robb(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for num in nums:
            temp = max(rob2,rob1+num)
            rob1 = rob2
            rob2 = temp
        return rob2