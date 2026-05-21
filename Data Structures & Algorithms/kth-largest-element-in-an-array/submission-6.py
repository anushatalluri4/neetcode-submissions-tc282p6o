class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def parition(l,r):
            pivot = r
            i = l
            for j in range(l,r):
                if nums[j]<=nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r],nums[i]
            return i
        k = len(nums)-k
        l, r = 0, len(nums)-1
        pivot = len(nums)
        while pivot!=k:
            pivot = parition(l,r)
            if pivot <k:
                l = pivot+1
            else:
                r = pivot - 1
        return nums[k]