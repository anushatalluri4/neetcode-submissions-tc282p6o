class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            if ''.join(sorted(i)) in dict:
                dict[''.join(sorted(i))]=dict[''.join(sorted(i))]+[i]
            else:
                dict[''.join(sorted(i))]=[i]
        return list(dict.values())
        