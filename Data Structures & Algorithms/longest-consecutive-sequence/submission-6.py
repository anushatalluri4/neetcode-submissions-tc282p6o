class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        l = 0
        res = 0
        for num in nums:
            if num-1 not in d:
                l = 1
                while num+l in d:
                    l+=1
                res = max(res,l)
        return res
        