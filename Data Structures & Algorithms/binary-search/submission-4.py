class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        ans = len(nums)
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                ans = mid
                r = mid -1
            else:
                l = mid + 1
        return ans if (ans < len(nums) and nums[ans] == target) else -1