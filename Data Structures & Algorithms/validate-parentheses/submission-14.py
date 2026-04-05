class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sym = {"]": "[","}":"{",")":"("}
        for c in s:
            if c in sym:
                if stack and stack[-1] == sym[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False         

