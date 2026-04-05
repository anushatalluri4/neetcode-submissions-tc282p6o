class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path,i,res):
            res.append(path[:])
            for i in range(i,len(nums)):
                path.append(nums[i])
                dfs(nums,path,i+1,res)
                path.pop()
        res=[]
        dfs(nums,[],0,res)
        return res

        