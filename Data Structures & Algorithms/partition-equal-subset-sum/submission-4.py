class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d = set()
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        for num in nums:
            s = set([0])
            for t in d:
                if t+num==target:
                    return True
                s.add(t+num)
                s.add(t)
            d=s
        return False