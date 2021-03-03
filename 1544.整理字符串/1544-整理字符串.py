class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if not stack or abs(ord(ch) - ord(stack[-1])) != 32:
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)