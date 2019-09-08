class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(2 ** n):
            res.append(i ^ (i // 2))
        return res 