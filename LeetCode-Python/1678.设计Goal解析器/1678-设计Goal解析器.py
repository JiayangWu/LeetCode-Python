class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        stack = []
        for char in command:
            if char == "G":
                res += char
            elif char == "(":
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    res += "o"
                    stack.pop()
                else:
                    res += "al"
                    stack.pop()
                    stack.pop()
                    stack.pop()
            else:
                stack.append(char)
        return res
