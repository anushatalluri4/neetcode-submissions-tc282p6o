class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        l = 0
        maxlength = 0
        while l < len(nums):
            length = 1
            while nums[l]+length in d:
                length += 1
            maxlength = max(maxlength, length)
            l += 1
        return maxlength

            