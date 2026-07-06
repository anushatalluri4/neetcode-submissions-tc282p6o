class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        res = 0
        for num in nums:
            if num-1 not in d:
                length = 0
                while num+length in d:
                    length+=1
                res = max(res,length)
        return res