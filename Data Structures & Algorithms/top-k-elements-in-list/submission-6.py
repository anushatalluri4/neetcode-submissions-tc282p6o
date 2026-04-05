class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        freq = [[] for i in range(len(nums)+1)]
        for key in d.keys():
            freq[d[key]].append(key)
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
