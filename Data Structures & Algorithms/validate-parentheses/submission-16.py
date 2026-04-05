class Solution:
    def isValid(self, s: str) -> bool:
        c2o = {"}":"{", "]":"[",")":"("}
        stack = []
        for i in s:
            if i in c2o:
                if stack and stack[-1] == c2o[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return len(stack)==0