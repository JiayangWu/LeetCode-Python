class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        s = 0
        for i, num in enumerate(arr):
            if s + num > 5000:
                return i
            s += num
        return len(arr)