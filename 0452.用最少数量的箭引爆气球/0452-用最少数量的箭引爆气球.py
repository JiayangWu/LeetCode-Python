class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or not points[0]:
            return 0

        points.sort(key = lambda x:x[1])

        arrow = points[0][1]

        res = 1
        for point in points:
            if arrow < point[0]:
                res += 1
                arrow = point[1]
        
        return res