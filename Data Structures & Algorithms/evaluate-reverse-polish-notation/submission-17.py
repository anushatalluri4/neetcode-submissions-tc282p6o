class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sym = {"+","-","/","*"}
        stack = []
        for t in tokens:
            if t not in sym:
                stack.append(int(t))
            elif t == "+":
                stack.append(stack.pop()+stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
        return stack[0]