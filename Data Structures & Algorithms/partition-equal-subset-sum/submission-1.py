class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        possible = {0}
        for num in nums:
            possible |= {s+num for s in possible}
            if target in possible:
                return True
        return False
        