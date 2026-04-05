class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for ind, num in enumerate(nums):
            if num > 0:
                break
            if ind > 0 and nums[ind-1] == num:
                continue
            l, r = ind+1, len(nums)-1
            while l<r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res
                    
