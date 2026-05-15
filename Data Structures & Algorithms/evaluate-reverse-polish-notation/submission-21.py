class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x,y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif i =="*":
                stack.append(stack.pop()*stack.pop())
            elif i == "-":
                x,y = stack.pop(), stack.pop()
                stack.append(y-x)
            elif i=="/":
                x,y = stack.pop(), stack.pop()
                stack.append(int(float(y)/x))
            else:
                stack.append(int(i))
        return stack[-1]
        