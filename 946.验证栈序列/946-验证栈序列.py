class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        s = []
        popped = popped[::-1]
        for num in pushed:
            s.append(num)
            while s and popped and s[-1] == popped[-1]:
                s.pop()
                popped.pop()
        
        return not s and not popped