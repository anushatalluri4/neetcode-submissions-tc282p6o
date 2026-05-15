class Solution:
    def isValid(self, s: str) -> bool:
        par = {"}":"{","]":"[",")":"("}
        stack = []
        for i in s:
            if i in par:
                if stack:
                    b = stack.pop()
                    if b != par[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
