class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(":")",
                  "{":"}",
                  "[":"]"}

        stack = []

        for c in s:
            if c in parens.keys():
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == parens[stack[-1]]:
                stack.pop()
            else:
                return False

        
        return len(stack) == 0