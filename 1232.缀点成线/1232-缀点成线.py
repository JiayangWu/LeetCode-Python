class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        c = sorted(coordinates, key = lambda x:x[0])
        k = None
        for i in range(len(c)):
            if i:
                x0, y0 = c[i - 1][0], c[i - 1][1]
                x1, y1 = c[i][0], c[i][1]
            
                if x0 == x1:
                    return False
                new_k = 1.0 * (y1 - y0) / (x1 - x0)
                if k and k != new_k:
                    return False
                k = new_k
            
        return True
        