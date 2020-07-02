class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import deque
        window = deque()
        res = []
        s = 0
        i = 1
        while i < target // 2 + 3:
            if s == target:
                res.append(list(window))
            if s <= target:
                window.append(i)
                s += i
                i += 1
            elif s > target:
                s -= window.popleft() 

        return res
