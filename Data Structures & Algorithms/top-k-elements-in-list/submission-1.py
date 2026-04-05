class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        s = sorted(dict, key=lambda x: dict[x],reverse=True)
        return s[:k]
        
        