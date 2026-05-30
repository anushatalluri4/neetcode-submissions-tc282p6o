class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        total = sum(nums)
        half = total//2
        d=set([0])
        for num in nums:
            s = set()
            for t in d:
                if t+num == half:
                    return True
                s.add(t+num)
                s.add(t)
            d = s
        return False

