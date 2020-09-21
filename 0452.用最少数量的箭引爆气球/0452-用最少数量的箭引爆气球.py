class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or not points[0]:
            return 0

        points = sorted(points, key = lambda x: x[1])
        res = 1
        pre_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > pre_end:
                res += 1
                pre_end = points[i][1]
        return res
