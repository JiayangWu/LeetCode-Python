class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2:
            return False
        dic = {")":"(","]":"[","}":"{"}
        stack = [None]
        for item in s:
            if item in dic and stack[-1] == dic[item]:
                stack.pop()
            else:
                stack.append(item)
        return len(stack) == 1
