class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # C(n - 1£¬m - 1)
        n = rowIndex
        m = n + 1
        def Calculate(n, m):
            down = 1
            up = 1
            for i in range(1, m):
                down *= i
                
            for i in range(1, m):
                up *= (n + 1 -i)
                
            return up // down
            
        res = list()
        for i in range(1, m + 1):
            res.append(Calculate(n, i))
        
        
        return res