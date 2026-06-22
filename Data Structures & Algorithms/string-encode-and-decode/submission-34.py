class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        print(s)
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            print(i,j)
            lent = int(s[i:j])
            end = j+1+lent
            res.append(s[j+1:end])
            i = end
        return res
