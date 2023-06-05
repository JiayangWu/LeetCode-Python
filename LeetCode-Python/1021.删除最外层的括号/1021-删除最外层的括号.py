class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left, right = 0, 0
        stack  = ""
        res = ""
        for char in s:
            if char == "(":
                left += 1
                stack += char
            elif char == ")":
                right += 1
                if left == right:
                    # find an outmost parenthesis pair
                    res += stack[1:]
                    stack = ""
                else:
                    stack += char
        return res

            

