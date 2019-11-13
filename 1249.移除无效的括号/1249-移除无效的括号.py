class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, 0
        stack = []
        remove = set()
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        stack = set(stack)
        res = ""        
        for i, ch in enumerate(s):
            if i not in stack and i not in remove:
                res += ch
        return res