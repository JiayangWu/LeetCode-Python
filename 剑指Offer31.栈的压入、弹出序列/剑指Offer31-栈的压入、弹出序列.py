class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed and not popped:
            return True
        if not pushed or not popped:
            return False
        stack = []
        popped = popped[::-1]
        for i, num in enumerate(pushed):
            stack.append(num)
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return not popped