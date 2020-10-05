class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {")": "(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
            else:
                if not stack or dic[ch] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0