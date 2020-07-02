class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = set(arr)

        res = 0
        for num in arr:
            if num + 1 in s:
                res += 1 
        return res