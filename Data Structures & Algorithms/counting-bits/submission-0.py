class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            resc=0
            while i:
                resc += 1 if i & 1 else 0
                i >>= 1
            res.append(resc)
        return res

        