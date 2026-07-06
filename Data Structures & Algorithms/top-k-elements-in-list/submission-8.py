class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for ind, val in count.items():
            freq[val].append(ind)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res)==k:
                    return res
        return res