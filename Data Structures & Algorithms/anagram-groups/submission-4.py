class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            char = [0]*26
            for i in range(len(s)):
                char[ord(s[i])-ord("a")]+=1
            d[tuple(char)].append(s)
        return list(d.values())
