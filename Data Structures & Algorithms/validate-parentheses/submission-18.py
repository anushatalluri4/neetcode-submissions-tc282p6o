class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen = {"]":"[","}":"{",")":"("}
        stack = []
        for i in range(len(s)):
            if s[i] in closetoopen:
                if stack and stack[-1] == closetoopen[s[i]]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(s[i])
        return True if not stack else False
        