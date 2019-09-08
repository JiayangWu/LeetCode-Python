class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i, char in enumerate(s):
            if char not in mapping:#left
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
                
        return len(stack) == 0