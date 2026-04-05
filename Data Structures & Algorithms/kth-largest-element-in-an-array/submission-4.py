class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l,r):
            pivot = nums[r]
            i = l
            for j in range(l,r):
                if nums[j]<=pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        k = len(nums) - k
        L, R = 0, len(nums)-1
        pivot = len(nums)
        while pivot != k:
            pivot = partition(L,R)
            if pivot > k:
                R = pivot - 1
            else:
                L = pivot + 1
        print(nums)
        return nums[pivot]