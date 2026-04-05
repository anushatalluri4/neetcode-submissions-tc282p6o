class Solution:
    def findMin(self, nums: List[int]) -> int:
        minv=float("infinity")
        for i in nums:
            minv=min(minv,i)
        return minv