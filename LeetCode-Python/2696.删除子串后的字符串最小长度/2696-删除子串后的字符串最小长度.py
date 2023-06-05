class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if char == "D" and stack and stack[-1] == "C":
                stack.pop()
            elif char == "B" and stack and stack[-1] == "A":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)