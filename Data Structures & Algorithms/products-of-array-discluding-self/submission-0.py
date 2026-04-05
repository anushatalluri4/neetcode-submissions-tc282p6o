import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(math.prod(nums[:i]+nums[i+1:]))
        return l

            
        