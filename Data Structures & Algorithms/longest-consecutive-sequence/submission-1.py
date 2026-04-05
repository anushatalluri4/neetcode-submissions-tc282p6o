class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        longest=0
        for i in nums:
            if i-1 not in d:
                length=1
                while(i+length) in d:
                    length+=1
                longest=max(longest,length)
        return longest
                
                    
        