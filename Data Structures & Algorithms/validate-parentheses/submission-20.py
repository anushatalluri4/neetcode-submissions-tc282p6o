class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"}":"{","]":"[",")":"("}
        for i in range(len(s)):
            if s[i] not in openToClose:
                stack.append(s[i])
            else:
                if stack and stack[-1]==openToClose[s[i]]:
                    stack.pop()
                else:
                    return False
        return False if stack else True