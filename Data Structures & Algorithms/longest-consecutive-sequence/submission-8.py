class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        lent = 0
        for num in nums:
            if num-1 not in d:
                length = 1
                while num+length in d:
                    length+=1
                lent = max(lent,length)
        return lent
            

