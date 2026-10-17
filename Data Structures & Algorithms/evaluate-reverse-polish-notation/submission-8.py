import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for t in tokens:
            if t == '+':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1+elem2)
            elif t == '-':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1-elem2)
            elif t == '*':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1*elem2)
            elif t == '/':
                elem2 = stack.pop()
                elem1 = stack.pop()

                stack.append(math.trunc(elem1/elem2))
            else:
                stack.append(int(t))

        return stack[0]
                