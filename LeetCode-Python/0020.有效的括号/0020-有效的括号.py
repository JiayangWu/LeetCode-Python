class Solution:
    def isValid(self, s: str) -> bool:
        right2left = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in right2left:
                if not stack or stack.pop() != right2left[char]:
                    return False
            else:
                stack.append(char)
        return stack == []
