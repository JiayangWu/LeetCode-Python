class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        dic = {"(":")", "{":"}", "[":"]"}
        for ch in S:
            if stack and stack[-1] in dic and dic[stack[-1]] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)