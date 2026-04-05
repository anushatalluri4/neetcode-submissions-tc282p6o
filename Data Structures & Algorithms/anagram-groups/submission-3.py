class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            char = [0]*26
            for j in strs[i]:
                char[ord(j)-ord("a")]+=1
            res[tuple(char)].append(strs[i])
        return list(res.values())