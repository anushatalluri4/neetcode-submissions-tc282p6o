class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        maxl = 0
        for num in nums:
            if num - 1 not in d:
                length = 1
                while num + 1 in d:
                    length += 1
                    num += 1
                maxl = max(maxl,length)
        return maxl
       