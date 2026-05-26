class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self,arr):
        rob1, rob2 = 0, 0
        for i in arr:
            temp = max(rob2,i+rob1)
            rob1 = rob2
            rob2 = temp
        return rob2
        