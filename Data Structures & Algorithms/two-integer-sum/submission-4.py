class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for ind, num in enumerate(nums):
            diff = target-num
            if diff in d:
                return [d[diff],ind]
            d[num]=ind