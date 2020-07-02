class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        for i in range(1, n):
            tmp = n - i
            if "0" not in str(i) and "0" not in str(tmp):
                return [i, tmp]