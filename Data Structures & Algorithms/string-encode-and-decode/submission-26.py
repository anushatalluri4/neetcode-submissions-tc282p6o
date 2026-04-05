class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        if len(strs)>1:
            for i in range(len(strs)):
                s=s+strs[i]+"*/"
        elif len(strs)==1:
            s=s+strs[0]+"*/"
        else:
            return s
        return s

    def decode(self, s: str) -> List[str]:
        if s!="":
            return(s.split("*/")[:-1])
        else:
            return []

        
