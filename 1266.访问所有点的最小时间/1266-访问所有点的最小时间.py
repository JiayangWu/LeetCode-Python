class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def helper(pair1, pair2):
            x0, y0 = pair1[0], pair1[1]
            x1, y1 = pair2[0], pair2[1]
            
            return max(abs(y1 - y0), abs(x1 - x0))
        
        res = 0
        for i, point in enumerate(points):
            if i > 0:
                res += helper(point, points[i - 1])
                
        return res