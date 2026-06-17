class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        i = 0
        print(nums)
        while i<len(nums):
            print(i)
            j = i
            while j+1 <len(nums) and nums[j] ==nums[j+1]:
                j+=1
            print(j)
            occ = j-i+1
            if occ>n:
                return nums[i]
            i = j+1
